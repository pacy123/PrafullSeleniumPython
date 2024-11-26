
try:
    num1 = int(input("Please enter First number:"+" "))
    num2 = int(input("Please Enter Second Number:"+" "))
    num3 = int(input("Please Enter Third Number:" + " "))
# if else for all numbers
    if num1>num2 and num1>num3 :
        print("First number is largest number", + num1)
    elif num2>num1 and num2>num3 :
        print("Second number is largest number", + num2)
    else:
        print("Third number is largest number", + num3)
except ValueError :
    print("Invalid input please enter only number ")

# using max function
try:
    num4 = int(input("Please enter First number:"+" "))
    num5 = int(input("Please Enter Second Number:"+" "))
    num6 = int(input("Please Enter Third Number:" + " "))

    print ("The largest number is ",max(num4,num5,num6))
except ValueError :
    print("Invalid input please enter only number ")

# Using nested if

try:
    num7 = int(input("Please enter First number:"+" "))
    num8 = int(input("Please Enter Second Number:"+" "))
    num9 = int(input("Please Enter Third Number:" + " "))

    if num7 > num8:
       if num7> num9:
           print("First number is largest number", + num7)

       else:
           print("Third number is largest number", + num9)
    else:
       if num8 > num7:
           print("Second number is largest number", + num8)

       else:
           print("Third number is largest number", + num9)
except ValueError :
    print("Invalid input please enter only number ")

