#+, -, *, /, //)
try:
    num1 = int(input("Enter first number  "))
    num2 = int (input("Enter second number  "))

# Addition
    num3 = num1+num2
    print ("The addition of numbers are",+ num3)

#Substraction
    if num1 > num2:
      num3 = num1-num2
      print ("subtraction of numbers", + num3)
    else :
      print("The second number should be bigger then first")

#Multiplication
    if num1 == 0 or num2 == 0  :
        print ("Please add positive numbers for multi")
    else:
        num3 = num1*num2
        print ("The multi of numbers are ", + num3 )
#Division

    if num2 ==0 :
        print ("Please add positive numbers for div")
    elif num1 > num2:
       num3  = num1/num2
       print ("Divisions of numbers are ", num3)
    else:
        print ("First number should be greater ")

# modules
    if num2 ==0 :
        print ("Please add positive numbers for div")
    elif num1 > num2:
       num3  = num1//num2
       print ("Moules of numbers are ", num3)
    else:
        print ("First number should be greater ")





except ValueError:
    print("This should be only number")