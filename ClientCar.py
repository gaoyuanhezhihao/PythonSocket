#ClientCar.py
import socket
SERVERIP = "222.195.92.21"
SERVERPORT = 1060
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVERIP,SERVERPORT))


try:
    s.send("CarCar")
    s.send("ConnectBoss")
    while True:
        ans = s.recv(1024)
        print ans
finally:
    s.close()
