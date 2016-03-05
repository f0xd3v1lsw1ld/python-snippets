#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"

import os
import sys
import zlib
from time import gmtime, strftime


def crc32(text):
 return zlib.crc32(text)

def main():
   if len(sys.argv) <2:
     print ("missing text to calculate crc")
     return;
   # input text
   text = str(sys.argv[1])
   _crc32 = crc32(text)
   print("The CRC32 is: 0x%X" % (_crc32& 0xFFFFFFFF))

if __name__=="__main__":
    main();
