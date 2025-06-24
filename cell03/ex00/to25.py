i = int(input("Enter a number less than 25 \n"))

if i < 25:
    while i < 25:
        print("inside the loop my variable is", i)
        i = i + 1
else:
    print("Error")
