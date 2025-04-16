def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x,y):
    return x / y
print("choose operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter your choice number:")
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("enter your first number :"))
        num2 = int(input("enter your second number:"))

        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(sub(num1,num2))
        elif choice == '3':
            print(multiply(num1,num2))
        elif choice == '4':
            print(divide(num1,num2))
        print("Thank you")



