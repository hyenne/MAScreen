import serial

port = serial.Serial(
    port='COM5',
    baudrate=9600,
)
while True:
  a='3'
  port.write(a.encode())
  print(a.encode())