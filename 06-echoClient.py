#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"
#from: https://docs.python.org/2/library/socket.html

# Echo client program
import socket
import sys

#server IP
ip = '127.0.0.1'
#create a socket
#AF_INET address (and protocol) family IPv4
#SOCK_STREAM socket type TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server IP and port
s.connect((ip, 50000))

try:
    while True:
        # wait for user input
        print("message: ")
        message = sys.stdin.readline()
        # send it to the server
        s.send(message.encode())
        # receive the response, max 1024 bytes
        antwort = s.recv(1024)
        # and print it
        print("[%s] %s" % (ip,antwort))
finally:
    s.close()
