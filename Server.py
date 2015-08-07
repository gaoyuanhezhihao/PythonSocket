#Server.py
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '222.195.92.21'
PORT = 1060
def recv_all(sock,length):
    data=""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('recv_all')
        data += more
    return data
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)
CaptainDict = {}
CarDict = {}
while True:
    print 'Listening at', s.getsockname()
    sc,sockname = s.accept()
    print 'We have accepted a connection from ',sockname
    print 'Socket connects',sc.getsockname(),'and',sc.getpeername()
    message = sc.recv(1024)
    print 'The incoming message says',repr(message)
    if message == "Boss":
        print "***Boss on the board\n"
        message = sc.recv(1024)
        print 'The incoming message says',repr(message)
        BossClient = sc
        CaptainDict["Boss"] = BossClient
    elif message == "CarCar":
        print "***Car is on your command\n"
        message = sc.recv(1024)
        print 'The incoming message says',repr(message)
        CarClient = sc
        CarDict["CarCar"] = CarClient
    if "CarCar" in CarDict and "Boss" in CaptainDict:
        print "Captain and Car are connected.Let's go\n"
        while True:
            message = CaptainDict["Boss"].recv(1024)
            print "recv",message,"from Boss.Sending to Car...\n"
            CarDict["CarCar"].sendall(message)
            
        
        
