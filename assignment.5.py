# Programmers: [Kelly King]
# Course: CS151, Merhi
# Programming Assignment: 5
# Program Inputs: [requesting that the users inputs information for trip calculations]
# Program Outputs: [The information displayed is the trip calculations including credit,card,and taxi distances]

import math
import csv
the_list = []
def loads_data(data):
    f = open(data, 'r')

    with f:
       try:
           csv_reader = csv.reader(f)
       except:
           pass
       else:
            for line in csv_reader:
                the_list.append(line)
       f.close()
    #print(the_list)
    return the_list
    loads_data('2016_09.csv')

#def returns_the_distance(distance, (lat1, lon1) and (lat2, lon2)

def average_cost_of_cash():
    average = 0
    loop_rotations = 0
    sum_of_cash = 0
    for i in the_list:
        if i[6]=="Cash":
            sum_of_cash += float(i[5])
            loop_rotations+=1
            average = sum_of_cash/loop_rotations
    print(average)

def average_cost_of_creditcard():
    loop_rotations = 0
    sum_of_creditcard = 0
    for i in the_list:
        if i[6]=="Credit Card":
            sum_of_creditcard += float(i[5])
            loop_rotations+=1
    average = sum_of_creditcard/loop_rotations
    print(average)


loads_data("2016_09.csv")
average_cost_of_cash()
average_cost_of_creditcard()
#print(the_list)

def count_of_all_trips(date):
   count= 0
   for i in the_list:
    if i[1].startswith(date,0,9) or i[2].startswith(date,0,9):
           count+= 1
    else:
        break
   return count
count_of_all_trips("2016-9-1")


#parameters function
def distance(lat1, lon1, lat2, lon2):
    return math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1-lon2))) * 3959
#parameter(+39.2904, -76.6122,+38.9072, -77.0369)
def vlat(num):
    try:
        float(num)
    except ValueError:
        print("Not Number")
    if float(num) < -90 or float(num) > 90:
        print("Sorry it is not valid!")
    else:
        return float(num)
def vlong(num):
    try:
        float(num)
    except ValueError:
        print("Not Number")
    if float(num) < -180 or float(num) > 180:
        print("Sorry it is not valid!")
    else:
        return float(num)
def vlat2(num):
    try:
        float(num)
    except ValueError:
        print("Not Number")
    if float(num) < -90 or float(num) > 90:
        print("Sorry it is not valid!")
    else:
        return float(num)
def vlong2(num):
    try:
        float(num)
    except ValueError:
        print("Not Number")
    if float(num) < -180 or float(num) > 180:
        print("Sorry it is not valid!")
    else:
        return float(num)
def vdate(date):
    try:
        date
    except:
        print("Not a valid date!!")
    else:
        if not date[0:4] == "2016" and date[5]=="9":
            print(date[0:4], date[5])
            print("Incorrect year or month!")
            return date
        else:
            return date

def rides_nearby(taxi_list):
#THE LATITUDE AND LONGITUDE HAVE TO BE BETWEEN VERY SPECIFIC POINTS AS EXPLAINED BELOW
    print (" \n + Latitude -90 to 90. \n + Longitude -180 to 180. \n + Distance< 0.")
    the_lat_radius = degree_radius(validation_lat())
    the_long_radius = degree_radius(validation_Long())
#VALIDATING THE DISTANCE
    distance = validation_distance()

#INPUTTING THE FILE THAT WILL STORE THE DATA, 2016_10.CSV OR 2016_09.CSV
    csvfilename = input ("-> Input name of .csv file that data is stored in")
    distance_of_rides = []
    for ride in taxi_list:
#CALCULATING THE DISTANCE FROM POINT A TO POINT B
        thepoint_pickup_distance = distance_calculations(the_lat_radius, the_long_radius,ride[8],ride[9])
        thepoint_dropoff_distance = distance_calculations(the_lat_radius_the_long_radius,ride[10],ride[11])
        if thepoint_pickup_distance <= distance or thepoint_dropoff_distance <= distance:
            distance_of_rides.append(ride)
    save_taxi_data(csvfilename, rides_in_distance)

def main():
    data = input("Enter data set name (include .csv when typing): ")
    loads_data(data)
    print("Which options would you like to view ??")
    print("Enter 1 for cash average")
    print("Enter 2 for credit average")
    print("Enter 3 for count of all the trips")
    print("Enter 4 for pickup or drop off location")
    t = int(input("Enter one of the options please"))
    if t==2:
        print("credit average",average_cost_of_creditcard())
    if t==4:
        print("pickup or drop off location", distance(vlat(39.2904),vlong(-76.6122),vlat2(38.9072), vlong2(-77.0369)))
    if t==3:
        date =input("Enter a date in the format of yyyy-m-d, has to be the year of 2016 and the 9th month of the year")
        print("count of all the trips", count_of_all_trips(vdate(date)))
    if t ==1:
        print("cash average", average_cost_of_cash())

main()

