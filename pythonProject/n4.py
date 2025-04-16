"""An online educational platform offers three courses: Programming Courses, Robotics
Courses and Academic Writing Courses : The vendor gives a discount of 10% on orders
for programming based courses if the order is for more than Rs. 1000. On orders of more
than Rs. 750 for Robotics Courses, a discount of 5% is given, and a discount of 10% is
given on orders for academic writing courses of value more than Rs. 500. Assume that the
numeric codes 1,2 and 3 are used for Programming, Robotics and Academic Writing
Courses respectively. Write a program that reads the product code and the order amount
and prints out the net amount that the learner is required to pay after the discount"""
a = int(input("select among 1,2,3"))
if a==1:
    amt = int(input())
    if amt>=1000:
        print("your discount is ",amt*0.1)
        print("final amount",amt-amt*0.1)
    else:
        print(amt)
if a==2:
    amt = int(input())
    if amt>=750:
        print("your discount is ",amt*0.05)
        print("final amount",amt-amt*0.05)
    else:
        print(amt)

if a==3:
    amt = int(input())
    if amt>=500:
        print("your discount is ",amt*0.1)
        print("final amount is ",amt-amt*0.1)
    else:
        print(amt)
