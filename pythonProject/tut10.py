"""A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user such as Number of classes held, Number of classes
attended and also student medical proof availability [1(for Yes)/0 (for No)]. Display
percentage of class attended and eligibility detail (Allowed/ Not Allowed) for exam. If
student is having less than 75% but having medical proof, he/she is ‘Allowed’ for exam,
otherwise ‘Not Allowed’. """
a = int(input("the number of classes held"))
b = int(input("the numebr of classes attendedd"))
c = int(input("the medical proof availability"))

d = int((b/a)*100)

if d>=75:
    print(d,"allowed")
else:
    if c==1:
        print(d,"allowed")
    else:
        print(d,"not allowed")


