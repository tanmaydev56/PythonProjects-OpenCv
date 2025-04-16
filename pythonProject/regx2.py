import re
name = input("enter your name").strip()
match = re.search(r"^(.+), *(.+)$", name)
if match:

    name = match.group(2) + " " + match.group(1)
    print(f"hello, {name}")

