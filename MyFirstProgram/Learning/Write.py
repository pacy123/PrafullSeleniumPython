#red the file and store all files
#Reverse the file
#and write the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content) #reverse list

    with open('test.txt', 'w')as writer:
        for line in reversed(content):
            writer.write(line)



