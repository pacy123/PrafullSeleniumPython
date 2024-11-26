
list1 = [1,3,6,8,'test']
list2 = [2,5,8]

list1.extend(list2)

list1.remove(2)
print(list1)

print (list1)

list2 = [4,9]
list1[2:3] = list2

print (list1)

# list comprehension

list1 = [2,4,6,7,9]
sqrlist2 = [num**2 for num in list1]
print(sqrlist2)


print("{}{}".format("value of", list1))


values = [2,3,4, 'Rahul', 6]

values.append("test")
print(values)  #[2, 3, 4, 'Rahul', 6, 'test']
values.insert(3,'prafull')
print(values)

del values[2]
print(values)



val = (1,2,'rahul',6,7)

print(val[1])
#dic key and value pair

a = {'a':2, 3:'test', 4:6, 'test':'again'}
print(a[4])
print(a['test'])

#dictionary dynamically at run time

dict={}
print(dict)
dict["firstname"] = "Rahul"
dict["lastname"] = "Test"
print(dict)







