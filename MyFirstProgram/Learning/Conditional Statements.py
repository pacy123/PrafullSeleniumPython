# if    ,   elif   ,  else

marks =  80
result = 'A+'
result1 = 'A-'

if marks < 80 :
    print (result1)

elif marks  >=  80:
    print(result)

else :
    print ("test")

#match
def mcheck (n):
     match n :
         case 'a' : return "this is working"
         case 'b' : return "this si not working"
         case 'c' : return "you should check this"

print (mcheck('a'))
print (mcheck('b'))
print (mcheck('c'))







