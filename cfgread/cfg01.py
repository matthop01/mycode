#!/usr/bin/env python3

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
#configlist2 = str(configlist).strip("\n")
#configlist3 = str(configlist2).strip(" ")
#print(configlist)

## Iterate thrhough configlist
for x in configlist:
    print(x.strip(" "), end="")

## Always close your file
configfile.close()
