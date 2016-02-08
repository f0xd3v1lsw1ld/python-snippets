#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"
#from: https://docs.python.org/2/library/socket.html

import socket
import sys

#create a socket
#AF_INET address (and protocol) family IPv4
#SOCK_STREAM socket type TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind to localhost adress and port 50000
s.bind(('127.0.0.1',50000))
# listen to max 1 queued connection
s.listen(1)

try:
 while True:
  # accept new connection
  # connection is a new socket object usable to send and receive data on the connection
  # addr is the address bound to the socket on the other end of the connection.
  connection, addr = s.accept()
  while True:
   # receive max 1024 
   data = connection.recv(1024)
   if not data:
    connection.close()
    break
   print("[%s] %s" % (addr[0], data[:-1]))
   #send the received data back to the client, without line ending
   connection.send(data[:-1])
finally:
 s.close()
