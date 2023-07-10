try :
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))

    if x%y==0 :
        print( x//y, "Yes, it is divisible")
    else:
        print(x//y, "No, it is not divisible")
except :
    print("Invalid input")