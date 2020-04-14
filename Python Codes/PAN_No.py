import re
pan = input()
if len(pan) == 10:
    if re.search("^[A-Z]{5}[0-9]{4}[A-Z]$",pan):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
