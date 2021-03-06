#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def get_ip_data():
    while True:
        try:
            input_ip = int(input("\nWhat is the best Star Wars movie? 1, 2, 3, 4, 5, 6, 7, 8, or 9? "))
            break
        except ValueError:
            print("Not a valid input you big dummy. Try again!")
    while True:
        try:
            input_driver = str(input("Who is the driver associated with the Millenium Falcon? "))
            break
        except:
           # input_driver.lower() != "chewbacca":
            print("Not a valid input you big dummy. Try again!!")
    while True:
        try:   
            input_vehicle = str(input("What is the vehicle associated with this train wreck? "))
            break
        except ValueError:
            print("Not a valid input, Elizabeth, it's the big one. Try again.")
    while True:
        try:
            input_year = int(input("What is the year associated with this vintage? "))
            break
        except ValueError:
            print("Nice thought but not a valid year. Try again!!!")
    d = {"IP": input_ip, "driver": input_driver, "Vehicle": input_vehicle,"Year": input_year,}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
