from Update import update
from Keypress import Control, Info

from tkinter import * 
from tkinter.ttk import *
import sys
import os
import time
import csv
import socket
import datetime
import threading
def Main():
    if os._exists("Logs")  == True:
        os.makedirs("Logs")

    #Main
    window = Tk()
    window.title("SmartRC App - Client")
    window.configure(bg="dark gray")
    window.geometry("300x600")
    window.resizable(False, False)

    style = Style()
    style.configure('TFrame', background="dark gray")
    style.configure('Frame1.TFrame', background='dark gray')

    bws = 20

    #Aircraft Data.
    AircraftDatatot = Frame(window, style="Frame1.TFrame")
    AircraftData1 = Frame(AircraftDatatot, style="Frame1.TFrame")
    AircraftData2 = Frame(AircraftDatatot, style="Frame1.TFrame")
    global Throttle
    Throttle = Label(AircraftData1, text="Throttle: N/A", background="dark gray")
    global Airspeed
    Airspeed = Label(AircraftData1, text="Airspeed: N/A", background="dark gray")
    global Altitude
    Altitude = Label(AircraftData1, text="Altitude: N/A", background="dark gray")
    global Roll
    Roll = Label(AircraftData2, text="Roll: N/A", background="dark gray")
    global Pitch
    Pitch = Label(AircraftData2, text="Pitch: N/A", background="dark gray")
    global Yaw
    Yaw = Label(AircraftData2, text="Yaw: N/A", background="dark gray")
    global Connection
    Connection = Label(window, text="Connection: N/A", background="dark gray")

    Throttle.config(font=("Arial", 20))
    Airspeed.config(font=("Arial", 20))
    Altitude.config(font=("Arial", 20))
    Roll.config(font=("Arial", 20))
    Pitch.config(font=("Arial", 20))
    Yaw.config(font=("Arial", 20))
    Connection.config(font=("Arial", 20))

    Throttle.pack()
    Airspeed.pack()
    Altitude.pack()
    Roll.pack()
    Pitch.pack()
    Yaw.pack()

    AircraftDatatot.pack()
    AircraftData1.pack(side=LEFT)
    AircraftData2.pack(side=RIGHT)

    Connection.pack()

    #System
    def Quit():
        Messages.insert(index="1.0", chars="Disconnecting")

    System =  Frame(window,  style="Frame1.TFrame")

    Messages = Text(window, width=30, height=10, borderwidth=3)
    ForceReconnect = Button(System, text="Force Reconnect", width=bws)
    ForceQuit = Button(System, text="Force Quit", width=bws, command=Quit)
    DownloadData = Button(System, text="Download Data", width=bws, command=lambda:host.sendmsg(clientsocket, address, Messages, "Reconnect"))

    ClearDisplay = Button(System , text="Clear Screen", width=bws, command=lambda:Messages.delete("1.0", "end"))

    Messages.pack()
    ForceReconnect.pack(pady=4)
    ForceQuit.pack(pady=4)
    DownloadData.pack(pady=4)

    ClearDisplay.pack(pady=6)

    System.pack(side=TOP, pady=10)


    #Check For Updates
    CheckForUpdates = Button(window, text="Check For Updates", width=bws, command=update.UpdateCheck)
    CheckForUpdates.place(relx=0.0, rely=1.0, anchor="sw")

    fh = open("Version", 'r')
    read = csv.reader(fh)
    commitid = []
    for line in read:
        commitid.append(line[0])

    commitidshort = list(commitid[0])
    commitidshort2 = ""
    for i in commitidshort:
        if len(commitidshort2) == 7:
            break
        else:
            commitidshort2 = commitidshort2+i

    version = Label(window, text="Version: "+commitidshort2)
    version.configure(font=("Arial"))
    version.place(relx=1.0, rely=1.0, anchor="se")

    #Setup
    count, ver = update.UpdateCheck()
    if count != 0:
        update.notification(count, ver)

    # window.protocol("WM_DELETE_WINDOW", sys.exit)
    window.mainloop()

    #Host
if __name__ == "__main__":
    main = threading.Thread(target=Main)
    main.start()
    time.sleep(3)

    controls = threading.Thread(target=Control)
    info = threading.Thread(target=Info, args=(Throttle, Airspeed, Altitude, Roll, Pitch, Yaw))

    controls.start()
    info.start()

    

"""
Main App
Made By NoKodaAddictions [2021]

Project Website: https://nokodaaddictions.github.io/Projects/RCAirplane/RCAirplane.html
Project Repository: https://github.com/nokodaaddictions/SmartRC
"""