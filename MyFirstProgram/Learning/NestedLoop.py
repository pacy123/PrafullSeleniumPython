'''month =['jan','feb','march']
day = ['sun','mon','tue']

for x in month:
    for y in day:
        print (x,y)
print ("This is for loop")'''


for i in range (1,5+1):
    for j in range(1,i+1):
       print ("* ", end="")

    print (" ")

for i in range (5, 0, -1):
    for j in range (1,i+1):
        print ("* ", end="")

    print(" ")

num=1

for i in range (5, 0, -1):
    num=1
    for j in range (1,i+1):
        print (num," ", end="")
        num=num+1

    print(" ")


num=1
for i in range (1,5+1):
    num=1
    for j in range(1,i+1):
       print (num," ", end="")
       num=num+1

    print (" ")

def PatternCheck(n):
    for i in range (1,n+1):

        for j in range(n-i):
          print (" ", end="")


        for k in range(1, 2*i):
           print ("*", end="")
        print()

PatternCheck(5)