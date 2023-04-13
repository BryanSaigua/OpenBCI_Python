import threading
import argparse
import socket
import sys
import pickle
from pyOpenBCI import OpenBCICyton
import time
from time import sleep
from datetime import datetime
import pandas as pd
import collections
import numpy as np
import datetime
from time import localtime, asctime

class ComunicacionBCI():
    def __init__(self):
              
        self.board = None
        process = threading.Thread(target=self.processarCon)
        process.start()
        process1 = threading.Thread(target=self.star_tiem)
        process1.start()
        self.f = open ('test.txt','w')
        self.star_time  = asctime(localtime())
        self.f.write("---------- MARCA 1 ----------- ")
        self.f.write(self.star_time + "\n")

        
    def print_raw(self,sample):
        try:
                data = sample.channels_data
                for i in range(1):
                    data = sample.channels_data
                    self.f.write(str(data) + "\n")
        except:
            pass

    def processarCon(self):
        while True:
            try:
                if not self.board:
                    self.board = OpenBCICyton(port='COM5', daisy=False)
                    self.board.start_stream(self.print_raw)
            except:
                pass
        
    def star_tiem(self):
        for hora in range(24):
            for minuto in range(60):
                for segundo in range(60):
                    print(f'{hora}:{minuto}:{segundo}')
                    time.sleep(1)
                    if segundo == 8:
                        self.f.write("----------MARCA 2 ----------- ")
                        self.f.write(asctime(localtime()) + "\n")
                    if segundo == 10:
                        self.f.write("----------MARCA 3 ----------- ")
                        self.f.write(asctime(localtime()) + "\n")
                    if segundo == 18:
                        self.f.write("----------MARCA 4 ----------- ")
                        self.f.write(asctime(localtime()) + "\n")
                            
ComunicacionBCI()
    #1745 - 2048 = 303
    #punter[0] = sample_chanel[256]
