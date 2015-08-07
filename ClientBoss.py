#ClientBoss.py
import socket
SERVERIP = "222.195.92.21"
SERVERPORT = 1060
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVERIP,SERVERPORT))


try:
    s.send("Boss")
    s.send("ConnectCarCar")
    while True:
        msg = raw_input("Your command:")
        s.send(msg)
finally:
    s.close()
