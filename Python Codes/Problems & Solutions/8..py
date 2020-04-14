vowels = ["a","e","i","o","u"]
verb = input("Enter a verb: ")
def make_ing_form():
    if (verb[-1] == "e"):
        if (verb[-2] == "i"):
            print(verb[0:-2] + "ying")
        elif (verb[-2] == "e" or verb[-2] == "b"):
            print(verb + "ing")
        else:
            print(verb[0:-1] + "ing")
    elif ((verb[-2] in vowels) and (verb[-1] not in vowels) and (verb[-3] not in vowels)):
     print(verb + verb[-1] + "ing")
    else:
        print(verb + "ing")

make_ing_form()
