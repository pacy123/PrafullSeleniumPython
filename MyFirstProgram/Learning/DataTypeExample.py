from collections.abc import bytearray_iterator

#Number   -   int, float, bool, complex

a = 10+3j

print (type(a))

#String

a= 'test'
b= "mas"
c= """bas"""

print (type(a),type(b),type(c))

#String is 0 to -1 in the end
#slicing and concatenation
string = "Hello World"
print (string)
print (string[0])
print (string[-1])
print (string[2:4])
print (string[ :3])
print (string[3: ])
print (string + "again")
print (string [7:-1])

#Sequence Data Type   - List, Tuple, Range   (ordered)
#1. List []
L = [203, "test", 206.10, 5+6j]
print (L, type(L))

M = [[201,'test',203], [1,2,3], [4,5,6]]
print (M, type(M))

print (L+M)
print (L[0])
print(L*4)
print (L[-1:2])
print (L[6:7])

#2. Tuple  -  ()   --  it can merge with list and all different data type

tup = (205, 'tup', 208.9, 211)

print (type(tup))
print (tup)
print (tup[0], tup[1], tup[2], tup[3])
print (tup[-1])
print (tup[0:-3])

print (id(tup))

tupmix = [[208,206,205], (209,211), (408,409,411)]

print (type(tupmix))
print (tupmix[0])
print (tupmix)
print (tupmix[-1])

# difference that list can be mutable but tuple can not be mutable
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

print (tuple)
print(list)

#Range (start,stop, step)  by default starts with 0 and start is optional
#use of range

for i in range(2,11, 2):
    print (i)

#Python binary Data type    -  Using bytes function

b1 =bytes([2,4,5,67,89,7])

b2 = b'Test'
print (b2)
print (type(b2))
print (id(b2))

print (b1)

#2. bytearray -  it is mutable

value = bytearray([72, 101, 108, 108, 111])
print(value)

import array

ar = array.array('i', [1,2,3,4,5])
view = memoryview(ar)
print (view)

#Disctionary Data type in python   -    {,}

dic = {1:'test', 2:'again', 3:'pacy'}
print(dic)
print (type(dic))

dic[4] = '6'
dic.__delitem__(1)
print(dic.values())
print(dic.get(2))
print(dic.items())
print (dic.keys())

print(dic)
dic.pop(2)
print (dic)

#Set data Type   (no duplicates, unordered)   -   {}

se = {1,2,3,6,5,6,7,3,0}
print(type (se))
print (se)

se.add(11)
print(se)
se.pop()
se.remove(6)

#Boolean Data type   - -  true and false

a = True
b= False

print(a)
print(b)
print (type(a), type(b))

print(se)

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))
















