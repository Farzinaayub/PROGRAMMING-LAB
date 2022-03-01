string = input('Enter your sentence: ')
list1=[]
for x in 'aeiou':
    if x in string:
    	list1.append(x)
print (list1)
