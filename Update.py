import os
import csv
import sys
from tkinter import *
from tkinter.ttk import *
import time

bws = 20

class update():
    def UpdateCheck():
        os.startfile("Delete.bat")
        time.sleep(2.5)
        os.system("git log -n 1 origin/main > Temp")

        fh = open("Temp",'r')
        fh2 = open("Version",'r')


        read = fh.readline()
        read2 = fh2.readline()

        read = read.split(" ")
        count = 0

        if read[1] != read2:
            count = count+1
            print("Client:", str(count))
        else:
            pass

        #If count is 1 - Client Update
        #If count is 2 - Aircraft Update
        #If count is 3 - Both Update

        return count, read
    
    def notification(count, ver):
        def group():
            sysbasic.update.InstallAircraftUpdate()
            sysbasic.update.InstallClientUpdate(root, update)

        update = Tk()
        update.title("SmartRC App - Update")
        update.configure(bg="dark gray")
    
        windowWidth = int(update.winfo_screenwidth())
        windowHeight = int(update.winfo_screenheight())
            

        update.geometry('300x100')

        if count == 1:
            UpdateBanner = Label(update, text="A Client Update Is Available")
            UpdateNow = Button(update, text="Update", width=bws, command=lambda:sysbasic.update.InstallClientUpdate(ver, update))
            
        if count == 2:
            UpdateBanner = Label(update, text="An Aircraft Update Is Available")
            UpdateNow = Button(update, text="Update", width=bws, command=sysbasic.update.InstallAircraftUpdate)
            
        if count == 3:
            UpdateBanner = Label(update, text="Updates Are Available For Client And Aircraft")
            UpdateNow = Button(update, text="Update", width=bws, command=group)
            
        UpdateBanner.pack(pady=5)
        UpdateNow.pack()
        NotNow = Button(update, text="Not Now", width=bws, command=update.destroy)   
        NotNow.pack()

        update.mainloop()
        return

    def InstallClientUpdate(ver, update):
        update.destroy()
        os.startfile("Update.bat")
        fh = open("Version",'w')
        fh.write(ver)
        fh.close()
        time.sleep(10)
        try:
            exec('App.py')
        except:
            pass
        return

"""
Updater
Made By NoKodaAddictions [2021]

Project Website: https://nokodaaddictions.github.io/Projects/RCAirplane/RCAirplane.html
Project Repository: https://github.com/nokodaaddictions/SmartRC
"""
