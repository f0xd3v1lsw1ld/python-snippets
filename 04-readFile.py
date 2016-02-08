#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"

# open given file,read line for line, print out each line
import sys

def main():
 if len(sys.argv) <2:
    print ("missing parameter")
    return;
 searchfile = str(sys.argv[1])
 try:
  fobj = open(searchfile, "r")
  for line in fobj:
    print(line)
  fobj.close()
 except IOError:
  print ("Error opening " + searchfile)
  return;

if __name__=="__main__":
    main();
