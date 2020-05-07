#!usr/bin/env python3

loginfail = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail +=1
        print(line.split(" ")[-1])
loginsuccess = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:
    for line in kfile:
        if "-] Authorization failed" in line:
            loginsuccess +=1
print("The number of failed log in attempts is ", loginfail)
print("The number of successful log in attempts is ", loginsuccess)
