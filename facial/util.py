import logging
import os
import glob
import csv
import random
import numpy as np


def checkDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def parseData(args):
    logging.info("Parsing data from ./data to ./parsed_data")
    # read ./data
    plain_data = []
    for i in range(args.num_labels):
        data_per_label = []
        for fp in glob.glob("./data/{}count*.csv".format(i+1)):
            with open(fp) as f: # with open(./0count46.csv) as f: => with open(./0count51.csv) as f: => ...
                next(f) # skip first line
                data_per_label += list(csv.reader(f)) #[1, 23] + [3, 4] = [1, 23, 3, 4] # [1, 23].append([3, 4]) = [[1, 23], [3, 4]]
        plain_data.append(data_per_label) # 여기서 data_per_label의 차원은 train/test size, plain_data는 num_labels * train/test size
    # shuffle data, cut it in args.data_size
    for i in range(len(plain_data)):
        random.shuffle(plain_data[i])
        plain_data[i] = plain_data[i][:args.data_size] # 섞은거에서 앞에서부터 5500개를 뽑음음
    # save parsed data in to ./parsed_data
    checkDir('./parsed_data')
    checkDir('./parsed_data/train')
    checkDir('./parsed_data/test')
    test_size = int(args.data_size * args.testing_ratio) # 550
    train_size = args.data_size - test_size # 4950
    for i in range(len(plain_data)):
        with open("./parsed_data/test/label-{}_size-{}.csv".format(i, test_size), "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(plain_data[i][:test_size])
        with open("./parsed_data/train/label-{}_size-{}.csv".format(i, train_size), "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(plain_data[i][test_size:]) # 실제로 4950

def loadData(args):
    test_size = int(args.data_size * args.testing_ratio)
    train_size = args.data_size - test_size
    logging.info("Loading data from ./parsed_data, train_size: {}, test_size: {}".format(train_size, test_size))
    train_x = []
    train_y = []
    test_x = []
    test_y = []
    for i in range(args.num_labels): # 0, 1, 2, ..., 11
        with open("./parsed_data/train/label-{}_size-{}.csv".format(i, train_size)) as f:
            train_x += list(csv.reader(f))
            train_y += [i for _ in range(train_size)]
        with open("./parsed_data/test/label-{}_size-{}.csv".format(i, test_size)) as f:
            test_x += list(csv.reader(f))
            test_y += [i for _ in range(test_size)]
    train_x = np.array(train_x) # list 자료형을 numpy 자료형으로 바꿔주는거
    train_y = np.array(train_y)
    test_x = np.array(test_x)
    test_y = np.array(test_y)
    return train_x, train_y, test_x, test_y

def fileToLEDString(filepath):
    header = "fa030039010006"
    crc    = 7
    footer = "55a9"
    ledstring = ""
    with open(filepath,"r") as fh:
        for ledline in fh.readlines():
            ledstring+=ledline.strip("\n")+" "*(24-len(ledline.strip("\n")))
    uartstring = header
    binarystring = ""
    for nibble in ledstring:
        if(  nibble==" "): binarystring+="00"
        elif(nibble=="-"): binarystring+="01"
        elif(nibble=="x"): binarystring+="10"
        elif(nibble=="X"): binarystring+="11"
        if(len(binarystring)==8):
            byte=int(binarystring,2)
            crc^=byte
            uartstring+="{:02x}".format(byte)
            binarystring=""
    uartstring += "{:02x}".format(crc)
    uartstring += footer
    return uartstring
