import serial

port = serial.Serial(
    port='COM5',
    baudrate=9600,
)

op = str(11)

while True:
    port.write([1])
