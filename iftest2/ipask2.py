#!usr/bin/env python3

import socket

while True:
    ipchk = input("Apply an IP address: ")

    if ipchk == "192.168.70.1":
        print("Looks like the IP address is set: " + ipchk + ".")
    elif ipchk:
        try:
            socket.inet_aton(ipchk)
            print("Looks like the IP address was set: " + ipchk)
            break
        except:
            print("That's not an IP Address, ya big dummy!")
    else:
        print("You did not provide any input.")

