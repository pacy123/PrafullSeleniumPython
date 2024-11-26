# for test in sec :
# statement

#1. for loop in string

word = "Mishita"

for i in word:
    if i not in 'aeiou':
        print (i, end=" ")

print(sep="")

#2. for loop with Tuples

numbers = (1,2,3,4,5,6,7,8,9)
total = 0
for num in numbers:
    total =total + num
print ("total of numbers are ",total)

#3. for loop with lists

numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for num in numbers :
    if num %2 ==0:
        print (num)

#4 for loop with range

for i in range (0,10,2):
    print (i)

#5 for loop with dictionaries

dic = {10:"Ten", 20:"Twenty", 30:"Thirty", 40:"Forty"}

for i in dic:
    print (i)

for i in dic.items():
    print (i)

for i in dic:
    print(dic[i])

#prime number program
#divide by 1 (module remain 0)
'''num = int(input("Please enter number to check if it is prime or not"))
for i in range (2,num):

    if num % i == 0:

        j = num / i
        print ("this is not prime number")


    else:
        print ("This is prime number", num)
        break
'''

#For loop to iterate between 10 to 20


for num in range(2,100):

  for i in range(2, (num // 2) + 1):

    # If num is divisible by any number between
    # 2 and n / 2, it is not prime
    if (num % i) == 0:
        print(num, "is not a prime number")
        break
  else:
        print(num, "is a prime number")


        

#for loop

obj = [2,3,5,7,9]

for i in obj:
    print(i*2)

#sum of first natural numbers 1+2+#+$
summ = 0
for j in range(1,6):
    summ = summ+j
print('sum',summ)

#programming examples

for k in range(1,10,11):

    print(k)


for k in range(10):

    print(k)







































