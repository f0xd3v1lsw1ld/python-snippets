#!/usr/bin/env python
__author__="f0xd3v1lsw1ld@gmail.com"

import os
import csv
import time
from time import gmtime, strftime


def MemInfo():
 tempFile = open( "/proc/meminfo" )
 memfree = tempFile.read() 
 tempFile.close()
 stri=memfree.split('\n')
 memtotal=int(stri[0].replace("MemTotal:","").replace("kB","").replace(" ",""));
 memfree=int(stri[1].replace("MemFree:","").replace("kB","").replace(" ",""));
 memused=memtotal-memfree
 return (memtotal,memused,memfree)
 
def main(): 
   print("KiB Mem %i total, %i used, %i free"%MemInfo())   
    


if __name__=="__main__":
    main();
