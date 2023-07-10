x = int(input("Give the first value: "))
y = input("What calculation do you want to do?: ")
z = int(input("Give the second value: "))
if y=="+" :
    print(x+z)
elif y=="-" :
    print(x-z)
elif y=="*" :
    print(x*z)
elif y=="/" :
        print(x/z)
else :
    print("Invalid input")

