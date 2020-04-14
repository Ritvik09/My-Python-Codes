import re
number = input()
if re.match("[1-9][0-9]{9}",number):
    print("Valid")
else:
    print("Invalid")
