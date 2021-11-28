# Programmers: [Kelly King]
# Course: CS151, Merhi
# Programming Assignment: 5
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

import math
import csv
the_list = []
def loads_data(data):

    with open('2016_09.csv','r') as f:
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
#loads_data('2016_09.csv')

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
    average = 0
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
   print(count)
count_of_all_trips("2016-9-1")

#parameters function
def parameter(lat1, lon1, lat2, lon2):
   distance = math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1-lon2))) * 3959
   print(distance)
parameter(+39.2904, -76.6122,+38.9072, -77.0369)

def main (options):



