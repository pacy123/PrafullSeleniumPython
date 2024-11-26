file = open('test.txt')
#read all the contents of file
#read n number of characters by passing parameters
#print(file.read(5))
#read one single line data
#print(file.readline())
#print(file.readline())



#print line by line using readaline

'''line = file.readline()

while line != "":
    print(line)
    line = file.readline()
   '''

for line in file.readlines():
    print(line)










file.close()