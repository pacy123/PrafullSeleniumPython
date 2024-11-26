
string1 = "This all is to check the vowels"
vowels = "aeiou"
count = 0

for x in string1:
    if x in vowels:
        count = count+1
        print(x)
        print (count)


digits =[str(x) for x in range (10)]
Str1= 'He4ll67o Mo5t67o'
char=[]

for x in Str1:
    if x not in digits:
        char.append(x)
Str2 = ''.join(char)
print (Str2)

str4 = 'Kashyap'
char=[]
for x in str4:
    if str4.count(x) > 1:

              print (x,"is duplicate" + " and it exist", str4.count(x),"times")


    else:
        print(x, "is not duplicate")


str5 = "prafull said to prafull about this "
char=""
for x in str5:
    if x not in char:
        char = char +x
print (char)


