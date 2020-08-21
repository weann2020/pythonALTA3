#!/usr/bin/env python3

import requests ## 3rd party URL lookup


def get_miss_distance(o,date):
    try:  
        #obj = (requests.get('https://api.nasa.gov/neo/rest/v1/feed?')).json()
        i=0
        for i in range(12):
            print(o["near_earth_objects"][date][i]["close_approach_data"][0]["miss_distance"]["miles"])
    except:
        print("error!")
    
#def moonlength(missdistance):
#    return round(missdistance/2389000)
    

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    #startdate = 'start_date=2018-06-01'  ## start date for data
    startdate = "start_date="+input("Enter the start date in format of yyyy-mm-dd: ")
    #enddate = "&end_date="+input("Enter the end date in format of yyyy-mm-dd: ")
    #enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=Odhtl3AdNc2QxIiFSb6ZkjQoghsuoqLs7UvgLz0X' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

#    print(neojson)

    #get_miss_distance(input("Enter the date to get the miss distatnce in format of yyyy-mm-dd: "))
    get_miss_distance(neojson, startdate)


## call main
main()

