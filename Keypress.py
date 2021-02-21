from pynput.keyboard import Listener
import socket
import sys
import datetime
import time
import os

def on_press(key):
    keypress = "{0}".format(key)
    control.sendall(bytes(keypress,"utf-8"))
    result = control.recv(1024).decode("utf-8")

    fh = open(f"Logs\Commands-{datetime.date.today()}.csv",'a')
    current = time.strftime("%H:%M:%S", time.localtime())
    fh.write(f"{keypress},{result},{current}\n")
    fh.close()

def Control():
    flightnum = 0
    if os.path.exists(f"Logs\Commands-{datetime.date.today()}.csv") == True:
        flightnum += 1
        while True:
            if os.path.exists(f"Logs\Commands-{datetime.date.today()}-{flightnum}.csv") == True:
                flightnum +=1
                continue
            else:
                fh.open(f"Logs\Commands-{datetime.date.today()}-{flightnum}.csv",'w')
                fh.close()
                break


    global control
    control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        control.connect(("", 64330))
    except:
        Control()

    with Listener(on_press=on_press) as listener:
        listener.join()
    

def Info(Throttle, Airspeed, Altitude, Roll, Pitch, Yaw):
    flightnum = 0
    if os.path.exists(f"Logs\Flight-{datetime.date.today()}.csv") == True:
        flightnum += 1
        while True:
            if os.path.exists(f"Logs\Flight-{datetime.date.today()}-{flightnum}.csv") == True:
                flightnum +=1
                continue
            else:
                break
    fh = open(f"Logs\Flight-{datetime.date.today()}.csv",'w')
    fh.close()
    info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        info.connect(("", 64220))
    except:
        Info(Throttle, Airspeed, Altitude, Roll, Pitch, Yaw)        
    while True:
        recv = info.recv(1024)
        stat = recv.decode().split(",")
        current = time.strftime("%H:%M:%S", time.localtime())
        fh = open(f"Logs\Flight-{datetime.date.today()}.csv", 'a')
        fh.write(f'{recv.decode("utf-8")},{current}\n')
        fh.close()