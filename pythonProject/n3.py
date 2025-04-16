a = int(input("enter the km travelled"))
if a<=1000:
    print(0)
elif 1000<a<=10000:
    print(50)
elif 1000<a<=20000:
    print(150)
elif 2000<a<=40000:
    print(250)
elif 4000<a<=60000:
    print(350)
else:
    print(500)