#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"

import base64
import sys

def encode():
    print("Please write some words and PRESS ENTER!")
    line = sys.stdin.readline()
    encoded = base64.encodestring(line)
    print("INPUT: %s, BASE64 encoded: %s"%(line[:-1], encoded))
    return encoded

def decode(_encoded):
    decoded = base64.decodestring(_encoded)
    print("BASE64 encoded: %s, DECODED: %s"%(_encoded[:-1], decoded))


if __name__ == '__main__':
    encoded = encode()
    decode(encoded)
