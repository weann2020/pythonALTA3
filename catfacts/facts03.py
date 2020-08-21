#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random


def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"

# chanllenge 1
    for dic in r.json()["all"]:
        if "user" in dic:
          user = dic.get("user")
          name = user["name"]
          first_name = name["first"]
        
        print("Actually " + first_name + " loves dogs more than cats...")  

# chanllenge 2
    list=[]
    for x in r.json()["all"]:  
        list.append(x.get("upvotes"))
    print("Max upvote is: ")
    print(max(list))

# chanllenge 3
    facts=[]
    for catfact in r.json()["all"]:
        facts.append(catfact.get("text"))
    print("Random single cat fact:\n"+random.choice(facts))




main()

