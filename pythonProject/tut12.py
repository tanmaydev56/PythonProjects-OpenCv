"""Petrol is collected for Indian Oil Corporation for sales from nearest ‘n’ storage
points to the Collection point. Given the amount of petrol from ‘n’ storage points
in litres(L) and milli litres (mL), write a PAC chart, flowchart, algorithm and
python code to compute the total quantity of oil in the collection point."""
n = int(input("enter"))
b = 0
d = 0
for x in range(n):
    a = int(input())
    c = int(input())
    b = b+x
    d = d+x
if a>=1000:
    c = 


