#the input and the variable

num = int(input("Enter The Number Of Whose Sum You Want To Find: "))

sum = 0

#for loop

for i in range(1, num+1):
    sum = sum + i
    print (f"The Sum Is {sum}")