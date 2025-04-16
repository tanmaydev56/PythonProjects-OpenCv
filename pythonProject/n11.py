"""list1 = []
n = int(input("enter the len"))
if n <=6:
    for i in range(n):
        t = int(input())
        list1.append(t)
        print(list1)


list1[1], list1[4] = list1[4], list1[1]
print(list1)
"""
"""
list1 = [1,2,3,4,5,6,7,8]
print(len(list1))"""

"""ASK
# Python program to demonstrate
# symmetry and palindrome of the
# string


# Function to check whether the
# string is palindrome or not
def palindrome(a):
    # finding the mid, start
    # and last index of the string
    mid = (len(a) - 1) // 2  # you can remove the -1 or you add <= sign in line 21
    start = 0  # so that you can compare the middle elements also.
    last = len(a) - 1
    flag = 0

    # A loop till the mid of the
    # string
    while (start <= mid):

        # comparing letters from right
        # from the letters from left
        if (a[start] == a[last]):

            start += 1
            last -= 1

        else:
            flag = 1
            break;

    # Checking the flag variable to
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")


# Function to check whether the
# string is symmetrical or not
def symmetry(a):
    n = len(a)
    flag = 0

    # Check if the string's length
    # is odd or even
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid

    while (start1 < mid and start2 < n):

        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")


# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)"""
"""string = input()
s = string.split()[::-1]
l = []
for i in s:
    l.append(s)
    print(l)"""
"""# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)
print(str(Tuple1.__sizeof__)
# print the sizes of sample Tuples"""
"""tup = (1,3,4,5,6,7)
y = list(tup)
count = 0
for i in y:
    count+=i

print(count)"""
"""i = int(input())
l = []
p = []
for t in range(i):
    r = int(input())

    l.append(r)

    t = (r, r * r * r)
    p.append(t)


print(l)
print(p)
"""
"""info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")"""
"""t = (1,2,3,4,5)
list = [x+20 for x in t]
print(list)"""
"""t =(1,[2,3,4],5,[5,3])
t[1][2] = 8
"""import math

def get_diagonal_number(matrix, query):
    n = len(matrix)
    sqrt_query = math.sqrt(query)
    diagonal_number = math.floor(sqrt_query)

    if diagonal_number > n:
        return None

    return diagonal_number

# Get input for the size of the matrix
n = 5

# Fill the matrix with numbers from 1 to n^2
matrix = [[0] * n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n):
        matrix[i][j] = num
        num += 1

# Get input for the queries
queries = list(map(int, input("Enter the queries (space-separated): ").split()))

# Process each query
for query in queries:
    diagonal_number = get_diagonal_number(matrix, query)

    if diagonal_number is not None:
        print("Diagonal number of", query, "is", diagonal_number)
    else:
        print("Number", query, "is not present in the matrix.")
