import platform
import ctypes
import os

def clear():
    os.system('cls')

def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str} | github.com/Callumgm ")
    else:
        os.system(f"\033]0;{str}\a")