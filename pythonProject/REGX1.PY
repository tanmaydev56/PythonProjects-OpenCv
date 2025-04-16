import re

email = input("enter your email").strip()
if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email,re.IGNORECASE):
    print("valid")
else:
    print("Ivalid")
