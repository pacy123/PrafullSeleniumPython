from pkgutil import iter_modules

even = 0
odd= 0

#list= [1,3,4,5,6,2,10,12,55,66,99,111,180]

'''lst = [int(num) for num in  input("input seperat evalue:").split()]
even = []
odd = []
for ev in lst:
    if ev%2 ==0:
        even.append(ev)


    else:
        odd.append(ev)

print("even numbers are" , even)
print("odd numbers are", odd)
'''
'''
inputValue = input("input separate inputs with string and int value with comma:").split(',')
output_list = []

for i in inputValue:
    i = i.strip()
    if i.isdigit():
        output_list.append(int(i)*2)
    else:
        output_list.append(i)

print(output_list)
'''


'''
unorder_list = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]

unorder_list.sort(reverse=True)

print(unorder_list)
'''

'''
# using bubble sort
# check values like - 1st value to last value  and swap if need to swap

listasc1 = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]

for i in range(len(listasc1)):
    for j in range (len(listasc1)-i-1):
        if listasc1[j] > listasc1[j+1]:
            listasc1[j], listasc1[j+1] = listasc1[j+1],  listasc1[j]

print(listasc1)


#descending order
listdsc1 = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]

for i in range(len(listdsc1)):
    for j in range (len(listdsc1)-i-1):
        if listdsc1[j] > listdsc1[j+1]:
            listdsc1[j], listdsc1[j+1] = listdsc1[j+1],  listdsc1[j]

print(listdsc1)

'''


listdigit =  [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
fistdigitnumber = []
twodigitnumber = []
threedigitnumber = []
fourdigitnumber = []
for i in listdigit:
    num_digits = len(str(i))
    if num_digits == 1:
#    if i<10:
        fistdigitnumber.append(i)
    elif num_digits == 2:
#    elif i<100:
        twodigitnumber.append(i)
    elif num_digits == 3:
 #   elif i < 1000:
        threedigitnumber.append(i)
    elif num_digits == 4:
#   else:
        fourdigitnumber.append(i)


print("One digit numbers", fistdigitnumber)
print("Two digit numbers", twodigitnumber)
print("Three digit numbers", threedigitnumber)
print("Four digit numbers", fourdigitnumber)


