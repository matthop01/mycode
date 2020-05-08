#!/usr/bin/env python3
import requests
import numpy as np

def main():
    """Run time code"""
    catname= []
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value associated with text"
    for catfact in r.json()["all"]:
       # print(catfact.get("text"))  # the .get() method returns NONE if key not found
        catfact=(catfact.get("user").get("name").get("first"))
def unique_counts(catname):
    unique, counts= np.unique(catname, return_counts=True)

#return np.asarray((unique_counts))

main()
