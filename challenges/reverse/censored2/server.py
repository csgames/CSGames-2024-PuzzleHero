#!/usr/bin/python3

import socket
import sys
from _thread import start_new_thread
from time import sleep
import argparse
import gc

from random import random, randint

parser = argparse.ArgumentParser()
parser.add_argument('--host', default="0.0.0.0")
parser.add_argument('--port', type=int, default=6666)
parser.add_argument('version', type=int)
parser.add_argument('flag')
args = parser.parse_args()

##################################################

def censor1(flag):
    out = ""
    for c in flag:
        if c.isalpha():
            rand = 0
            while not rand:
                rand = int(random() * 26)
            start = ord('A') + (ord(c) & 32)
            num = ord(c)
            num -= start
            num += rand
            num %= 26
            num += start
            out += chr(num)
        else:
            out += c
    return out


def censor2(flag):
    out = ""
    for c in flag:
        if random() < 0.5:
            out += c
    if len(out) > 0.75 * len(flag):
        return censor1(flag)
    return out


def censor3(flag):
    out = ""
    for i in range(randint(1, 5)):
        out += chr(randint(33, 126))
    for c in flag:
        out += c
        for i in range(randint(1, 5)):
            out += chr(randint(33, 126))
    return out


if args.version in [2, 3]:
    for i, j in zip(args.flag, args.flag[1:]):
        assert i != j, f"No two same consecutive letters in the first flag: {i} {j}"


##################################################

def send_data(c, data):
    c.send(bytes(data, encoding='utf8'))

# thread function
def threaded(c):
    try:
        send_data(c, "WARNING\n")
        send_data(c, "=======\n")
        send_data(c, "This FLAG request has been intercepted and censored in concordance with Chlorophyllai's AI-generated information policy\n")
        send_data(c, "\n")
        send_data(c, "AUDIT LOG\n")
        send_data(c, "=========\n")


        if args.version == 1:
            out = censor1(args.flag)
            send_data(c, """
def censor1(flag):
    out = ""
    for c in flag:
        if c.isalpha():
            rand = 0
            while not rand:
                rand = int(random() * 26)
            start = ord('A') + (ord(c) & 32)
            num = ord(c)
            num -= start
            num += rand
            num %= 26
            num += start
            out += chr(num)
        else:
            out += c
    return out
""")
        elif args.version == 2:
            send_data(c, """
def censor2(flag):
    out = ""
    for c in flag:
        if random() < 0.5:
            out += c
    if len(out) > 0.75 * len(flag):
        return censor1(flag)
    return out
""")

            out = censor2(args.flag)
        elif args.version == 3:
            send_data(c, """
def censor3(flag):
    out = ""
    for i in range(randint(1, 5)):
        out += chr(randint(33, 126))
    for c in flag:
        out += c
        for i in range(randint(1, 5)):
            out += chr(randint(33, 126))
    return out
""")

            out = censor3(args.flag)

        send_data(c, out + "\n")

        # connection closed
        print('End connection')
    finally:
        c.close()
        gc.collect()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((args.host, args.port))
    print("socket binded to", args.host, "on port", args.port)

    # put the socket into listening mode
    s.listen(100)

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        # print_lock.acquire()
        print('Connected to :', addr)

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
finally:
    print('Clean exit')
    s.close()
