"""Earthquake Research Institute of Japan has recorded earthquake occurred in the year 2021
using Richter scale. Develop PAC, Algorithm, Flowchart and write a Python program to
get the ’n’ (number of times) the earthquake has occurred and print the number of times in
which the magnitude was low, medium and high. The magnitude value is given in microns.
If the value is less than 5.4(inclusive) in microns then it is low, 5.4 to 7.0 (inclusive) it is
medium and more than 7.0 it is high.
Also, if the number of times recorded is Zero, display as “No earthquake predicted” and
if the number of times recorded is negative, display as “Invalid Input”"""
n = int(input("the number of time the earthquake occured"))
low = 0
mid = 0
high = 0

for x in range(n):



    if n>0:
        b = float(input("microns value for earthquake occured"))
        if b<=5.4:
            low = low+1

        elif 5.4<b<=7:
            mid = mid+1
        elif b>=7:
            high = high+1
        elif b==0:
            print("no earthquake pridicted")



else:
    print(low)
    print(mid)
    print(high)

if n<0:
    print("inavailid input")


