"""import re
renumber = input()
if renumber:
    re.match("^[0-9][0-9][a-z][a-z][a-z][A-z][A-Z][A-Z][0-9][0-9][0-9]$",renumber)
    print("matched")
else:
    print("not matched")"""
"""import re
number = input()
if re.match("[1-9][0-9]{9}", number):

    print("matched")
else:
    print("not matched")"""


"""word = "tanmaysharma"
count = 0
for x in word:
    if x == "a":
        count = count+1
        b = count
        print(b)"""
def avg(*num):

    sum = 0
    for i in  num:

        sum = sum + 1
    print(sum/len(num))
avg(2,3,4,5)




