from pynput.keyboard import Listener
import socket
import sys
import datetime
import time

def on_press(key):
    keypress = "{0}".format(key)
    control.sendall(bytes(keypress,"utf-8"))
    result = control.recv(1024).decode("utf-8")
    print(result)

    fh = open(f"Logs\Commands-{datetime.date.today()}.csv",'a')
    current = time.strftime("%H:%M:%S", time.localtime())
    fh.write(f"{keypress},{result},{current}\n")
    fh.close()

def Control():
    fh = open(f"Logs\Flight-{datetime.date.today()}.csv",'w')
    fh.close()
    global control
    control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        control.connect(("", 64330))
    except:
        Control()

    with Listener(on_press=on_press) as listener:
        listener.join()
        print(listener.join())

def Info():
    fh = open(f"Logs\Flight-{datetime.date.today()}.csv",'w')
    fh.close()
    info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        info.connect(("", 64220))
    except:
        Info()
    try:
        while True:
            recv = info.recv(1024)
            print(recv.decode())
            current = time.strftime("%H:%M:%S", time.localtime())
            fh = open(f"Logs\Flight-{datetime.date.today()}.csv", 'a')
            fh.write(f'{recv.decode("utf-8")},{current}\n')
            fh.close()
    except KeyboardInterrupt:
        fh.close()
        sys.exit()