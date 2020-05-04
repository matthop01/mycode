#!usr/bin/env python3

name= input("What is your name? ")

col_list= ["blue", "Columbus"]

col_list.append("1492")

print("In " + col_list[2] + ", " + col_list[1] + " sailed the ocean " + col_list[0] + ". " + name + " fell off the boat.")

col_list.pop([2])
col_list.append("1492")

