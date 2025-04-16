"""Draw a flowchart and construct a python program to accept the monthly income
of an employee and display the income tax to be paid at the end of the year
according to the following criteria:
Annual income (in Rs) Income Tax
> 1000000 4 %
> 500000 and <= 1000000 2 %
<= 500000 NIL"""
a = int(input("employee annual income "))
if a>5000000:
    print("NIL")
elif a>=500000 and a<=1000000:
    print("income tax",int(a*0.02))
else:
    print(int(a*0.04))
