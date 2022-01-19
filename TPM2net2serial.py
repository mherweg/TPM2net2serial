import serial
import socket
import time

#
# receive TPM2.net Data via LAN or Wifi
# and send it via ttyUSB0 or ttyACM0 to our Matedisplay
#
# TODO: change the header bytes before sending (see: https://gist.github.com/jblang/89e24e2655be6c463c56)
#


vSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
tServerAddress=('localhost',65506)
vSocket.bind(tServerAddress)
vSerial=serial.Serial('/dev/ttyUSB0',baudrate=500000,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=1)
while True:
    byData, _ = vSocket.recvfrom(1024)
    vSerial.write(byData)
    time.sleep(0.02)
    
    
