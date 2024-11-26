# Adding in try catch block to only enter number
try:
    #number = int(input("Please enter any number:"+" "))
    number = 4

    # marking 0 a diff number
    if number == 0 :
      print("Number is zero")
    # elseif for negative value
    elif number <0:
      print("This is negative number")
    # else if for positive value
    elif number >0:
      print("This is  positive number")
#exception for other values
except ValueError :
    print("Invalid input please enter only number ")




