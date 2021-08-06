#!usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("ENTER IP: ")
port = int(input("ENTER PORT: "))

def portScan(port):
    if s.connect_ex((host, port)):
        print("Port is closed.")
    else:
        print("Port is Open.")

portScan(port)