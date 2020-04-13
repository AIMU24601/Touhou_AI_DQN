import socket
import ctypes
from PIL import ImageGrab
import numpy
import cv2
import time
import random

SENDINPUT = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wvk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlagss", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_ushort),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_ulong),
                ("dy", ctypes.c_ulong),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

#Actual Functions

def presskey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008 | 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releasekey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def screenshot():
    x = 284
    y = 290
    w = 670
    h = 740
    img = ImageGrab.grab((x, y, w, h))
    img = numpy.asarray(img, dtype="uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    jpegstring = img.tostring()
    CLIENT.send(str(len(jpegstring)))
    CLIENT.recv(1024)
    CLIENT.send(jpegstring) #適当なデータを送信(届く側にわかる)
    sent = CLIENT.recv(1024).strip() #レシーブは適当な二進数に
    return int(sent)

def commandstart(action):
    if action == -1:
        presskey(0x01)#ESC
    elif action == 0:
        presskey(0x2c)#Z
    elif action == 1:
        presskey(0x2c)#Z
        presskey(0xcb)#LEFT
    elif action == 2:
        presskey(0x2c)#Z
        presskey(0xc8)#UP
    elif action == 3:
        presskey(0x2c)#Z
        presskey(0xcd)#RIGHT
    elif action == 4:
        presskey(0x2c)#Z
        presskey(0xd0)#DOWN
    elif action == 5:
        presskey(0x2c)#Z
        presskey(0xcb)#LEFT
        presskey(0xc8)#UP
    elif action == 6:
        presskey(0x2c)#Z
        presskey(0xc8)#UP
        presskey(0xcd)#RIGHT
    elif action == 7:
        presskey(0x2c)#Z
        presskey(0xcd)#RIGHT
        presskey(0xd0)#DOWN
    elif action == 8:
        presskey(0x2c)#Z
        presskey(0xd0)#DOWN
        presskey(0xcb)#LEFT
    elif action == 9:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
    elif action == 10:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xcb)#LEFT
    elif action == 11:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xc8)#UP
    elif action == 12:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xcd)#RIGHT
    elif action == 13:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xd0)#DOWN
    elif action == 14:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xcb)#LEFT
        presskey(0xc8)#UP
    elif action == 15:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xc8)#UP
        presskey(0xcd)#RIGHT
    elif action == 16:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xcd)#RIGHT
        presskey(0xd0)#DOWN
    elif action == 17:
        presskey(0x2a)#LSHIFT
        presskey(0x2c)#Z
        presskey(0xd0)#DOWN
        presskey(0xcb)#LEFT

def commandend(action):
    if action == -1:
        releasekey(0x01)#ESC
    elif action == 0:
        releasekey(0x2c)#Z
    elif action == 1:
        releasekey(0x2c)#Z
        releasekey(0xcb)#LEFT
    elif action == 2:
        releasekey(0x2c)#Z
        releasekey(0xc8)#UP
    elif action == 3:
        releasekey(0x2c)#Z
        releasekey(0xcd)#RIGHT
    elif action == 4:
        releasekey(0x2c)#Z
        releasekey(0xd0)#DOWN
    elif action == 5:
        releasekey(0x2c)#Z
        releasekey(0xcb)#LEFT
        releasekey(0xc8)#UP
    elif action == 6:
        releasekey(0x2c)#Z
        releasekey(0xc8)#UP
        releasekey(0xcd)#RIGHT
    elif action == 7:
        releasekey(0x2c)#Z
        releasekey(0xcd)#RIGHT
        releasekey(0xd0)#DOWN
    elif action == 8:
        releasekey(0x2c)#Z
        releasekey(0xd0)#DOWN
        releasekey(0xcb)#LEFT
    elif action == 9:
        #LSHIFT
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
    elif action == 10:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xcb)#LEFT
    elif action == 11:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xc8)#UP
    elif action == 12:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xcd)#RIGHT
    elif action == 13:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xd0)#DOWN
    elif action == 14:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xcb)#LEFT
        releasekey(0xc8)#UP
    elif action == 15:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xc8)#UP
        releasekey(0xcd)#RIGHT
    elif action == 16:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xcd)#RIGHT
        releasekey(0xd0)#DOWN
    elif action == 17:
        releasekey(0x2a)#LSHIFT
        releasekey(0x2c)#Z
        releasekey(0xd0)#DOWN
        releasekey(0xcb)#LEFT

HOST = "" #サーバー名を入力
PORT = 12345 #適当なPORTを指定
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4による双方向通信
CLIENT.connect((HOST, PORT)) #サーバーに接続

try:
    response = 0
    time.sleep(4)
    commandstart(-1)
    time.sleep(4*(1.0/60))
    commandend(-1)
    while True:
        for no in range(10):
            time.sleep(1)
            while True:
                commandstart(response)
                new_response = screenshot()
                commandend(response)
                if new_response == -2:
                    print("end")
                    break
                else:
                    response = new_response
            CLIENT.send("stop")
            CLIENT.recv(1024)
            time.sleep(6)
            response = -1
            commandstart(response)
            time.sleep(4*(1.0/60))
            commandend(response)
            response = random.randint(0, 17)
except KeyboardInterrupt:
    CLIENT.close()
