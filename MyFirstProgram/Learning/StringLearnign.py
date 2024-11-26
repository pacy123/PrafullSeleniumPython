
a = "hello World"

print (a)
print (a[0:7])
print (a[0:7:2])

print (a[-7:-1:2])
print (a[:4]+"test")

print ("my name is %s and %d" %('test',23))

print (type (a))

print (a.capitalize())
print (a.casefold())

#print (a.center(2,5))

print (a.count('l', 0,2,))

print (a.endswith('h', 0,4))

print (len(a))
print (max(a))
print (min(a))

# modify string

b= 'WORD'
print (b)
print (type (b))
ls = list(b)
print (ls)
print (type (ls))

ls.insert(3, "L")

print (ls)

b=''.join(ls)
print (b)
print (type (b))

# from array

import array as ar

s1 = "WORD"

ary = ar.array('w',s1)

print (ary)
print (type(ary))

ary.insert(3,'l')

print (ary)

s1=ary.tounicode()
print (s1)
print (type(s1))


import io
s4 = 'WORD'



string = 'test'
print ("test the %s" %string)


string1 = "tutorial{}"

print (string1.format("point"))

s7 = "Hello this is \tnew test"

print(s7.lower())
print(s7.swapcase())
print(s7.title())
print(s7.upper())
print(s7.center(50,'!'))

print(s7.expandtabs(8))
print(s7.lstrip('H'))
print(s7.rstrip('t'))
print(s7.split())
print()



str1 = "rahulshettyacademy.com"
str2 = "rahul"

print(str2 in str1)

#split string

var = str1.split("y")
print(var)
str4 = "  great  "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())


















