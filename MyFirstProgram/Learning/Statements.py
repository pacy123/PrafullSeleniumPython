#break

for letter in 'Python':
    if letter =='h':
      break
    print (letter)
print ("out of loop")


var =1
while var >0:

    print (var)
    var =var +1
    if var ==5:
        break
print ("out of loop")

no = 44
count =0
numbers = [11,55,44,13,12,9]
for num in numbers:
    print(count)
    count = count + 1
    if num ==no:
        print ("found number", num)
        break
print ("out of loop")


#Countinue
for letter in 'Python':
    if letter == 'h':
        continue
    print (letter)
print ("out of loop")


num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1

#Countinue
for letter in 'Python':
    if letter == 'h':
        pass
        print ("this is continue block")
    print (letter)
print ("out of loop")


A = True

#while True: pass

# Type Ctrl-C to stop


def fun1():
    ...

def fun2():
    print("test")

fun1()
fun2()





