# the input and the empty variable

string = input("Enter The Stuff You Want To Reverse: ")

string2 = ("")

# the for loop and the statement to reverse it

for i in string:
    string2 = i + string2

print (f"\nThe Original Stuff Is {string}")
print (f"The Reversed Stuff Is {string2}")