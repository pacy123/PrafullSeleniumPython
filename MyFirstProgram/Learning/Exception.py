
ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    #raise Exception("Product cart count does not match")
     pass

assert(ItemsInCart==0)

#try catch  we do not want the test case stop

try:
    with open('file.txt', 'r') as reader:
           reader.read()
except:
    print("this is failure in try block")


try:
    with open('test.txt', 'r') as reader:
           reader.read()
except Exception as e:
    print(e)
#finally keyword
finally:
    print("this is definatly run")







