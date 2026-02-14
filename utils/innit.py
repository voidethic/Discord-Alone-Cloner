import requests
import threading
import asyncio
import base64
from pystyle import *
import random
from datetime import datetime
import os
import time

def logo():
    l = """                             
              _    _     ___  _   _ _____ 
             / \  | |   / _ \| \ | | ____|
            / _ \ | |  | | | |  \| |  _|  
           / ___ \| |__| |_| | |\  | |___ 
          /_/   \_\_____\___/|_| \_|_____|                          
    """
    c = Colorate.Horizontal(Colors.green_to_red, l)
    print(c)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def current_time():
    return datetime.now().strftime("%H:%M:%S")

b = Colors.dark_red
r = Colors.red
g = Colors.dark_gray
y = Colors.yellow
w = Colors.white
    