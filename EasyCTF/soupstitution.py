#!/usr/bin/env python3

from binascii import unhexlify 
from operator import attrgetter 

ME_FLAGE = '<censored>'

def first(var):
    soup = 0
    while var != 0:
        soup = (soup * 10) + (var % 10)
        var //= 10
    return soup

def second(var):
    soup = 0
    for soUp in var:
        soup *= 10
        soup += ord(soUp) - ord('0')
    return soup

def SOUP():

    number = 1234567

    num = str("%07d" % number)

    soup = second(num) #simple reverse numbers

    print(soup)

    soup = first(soup)
    print(soup)
    #converts decimal number to hex
    #pads to 8
    SouP = attrgetter('zfill')(hex(soup)[2:])(8)[-8:]
    

    #print(unhexlify(SouP))

    #19 32 55 56 32 converts to right hex number
    #2365552391

    #\x73\x30\x75\x70, 73307570

    if unhexlify(SouP) == attrgetter('encode')('s0up')():
        print("oh yay it's a flag! " + number)


if __name__ == '__main__':
    SOUP()

