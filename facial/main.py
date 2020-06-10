import logging
import argparse
import sys
import util
import joblib
from sklearn.svm import SVC
from sklearn.metrics import classification_report


def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--parse_data', type=bool, default=False)
    parser.add_argument('--data_size', type=int, default=10000)
    parser.add_argument('--testing_ratio', type=float, default=0.1)
    parser.add_argument('--num_labels', type=int, default=11)
    parser.add_argument('--train', type=bool, default=False)
    parser.add_argument('--checkpoint', type=str, default='model_emotion.pkl')
    args = parser.parse_args()
    return args

def main():
    # print 대신 logging을 사용하면 날짜랑 시간이 나옴
    # basicConfig는 logging을 사용하려면 실행해야하는 초기함수
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m-%d %H:%M', stream=sys.stdout)
    args = get_args()
    if args.parse_data:
        util.parseData(args)
    train_x, train_y, test_x, test_y = util.loadData(args)
    checkpoint_path = "./checkpoints/{}".format(args.checkpoint) # ./checkpoints/model.pkl
    if args.train:
        logging.info("Training model...")
        # fit=training
        svc = SVC(kernel='linear').fit(train_x, train_y)
        util.checkDir("./checkpoints")
        logging.info("Saving model from {}...".format(checkpoint_path))
        # save
        joblib.dump(svc, checkpoint_path) # 모델을 파일로 저장해줌
    else:
        logging.info("Loading checkpoint from {}...".format(checkpoint_path))
        svc = joblib.load(checkpoint_path) 
    pred_y = svc.predict(test_x)
    logging.info("Prediction result on test data")
    print(classification_report(test_y, pred_y))

if __name__=='__main__':
    main()
