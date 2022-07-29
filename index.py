#!/bin/python3

from email import header
import os,sys
from pathlib import Path
import dominate
from dominate import tags as t
import requests as req
import multiprocessing as mp
import threading
import time

root = Path(os.path.dirname( __file__ ))

class myThread(threading.Thread):

    def __init__(self) -> None:
        threading.Thread.__init__(self)
        #self.name = __name__
        self.additional ="some result"
        #print(self.name) 
    def start(self,name):
        
        self.name = name
        print(self.name)
        pass
        pass
    def launcher(self):
        def defFunction():
            time.sleep(1.5)
            print("bah humbug")
        th = mp.Process(target=defFunction)
       #th.
        th.start()
        
        #exe thread for something, get result
        return "threadLaunched: "
'''
#import another module from anywhere

modPath = root/"module"
sys.path.append(modPath)

'''
def loadSecond():
    pass
def launch():
    print("BOOOO!")
#creates the landing page, and navs the html folder for other links and such.

def buildMainPage():
    doc = dominate.document()
    #addCSS and other req dependencies
    h = t.header()
    
    doc.add(h)
    #build body
    b = t.body()
    l = t.li()
    #build simple nav links for routing
    
if __name__ == "__main__":
    print(__name__,",",root)
    print()
    threading.Thread(target=launch)
    mt = myThread()
    mts = []
    
#    mt.name = "my thread"
    mt.start("nameOfProcessThread")
    alive = mt.is_alive()
    while(alive):
        alive = mt.is_alive()
        print(f"{mt.name}ActiveTime:" +time.time())
        pass
    print(mt.launcher())
    pass
