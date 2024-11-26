# memory check by id

"math"
print (id("math"))
#and
pac = "div"
print (id(pac))
#2661507066080
#2661509212528

# no need to assign data type
a = 100
b="hundred"
print (a, b)
# can delete variable
del a
# can not print now

# Type of variable
d=10
e ='again'
f= 10.13

print (type(d))
print (type(e))
print (type(f))

#type cast of variables
q = int(11)
r = str(10)
y = float(10)

print(q,r,y)

#python is case-sensitive
age =10
Age =11
aGe = 12

print (age,Age,aGe)

#multiple variable assignment

z=x=v = 10
print (z,x,v)

z,x,v = 20,30,40
print(z,x,v)

width =10
height =20
area = width*height
print (area)

#Local Variables

def sum(x,y):
    summ=x+y
    return summ
print (sum(5,10))

#Global Variables
x=19
y=20

def sum():
    summ=x+y
    return summ
print (sum())

#constants

PER_VALUE = 10


print (PER_VALUE)

a=b=40
print(a is b)

print(id(a), id(b))











