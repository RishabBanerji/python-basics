#list introduction
countries = ['uk','usa','india','pakistan']
print(countries)

#to print specific element from list
print(countries[0])

#to replace an element
countries[1]='nepal'
print(countries)

#to get length
print(len(countries))

#to print 2 lists together
list1 = ['banana','papaya','apple']
list2 = [1,2,3,4]
list1.extend(list2)
print(list1)


#to add an element to a list(at the end)
list1 = ['banana','papaya','apple']
list1.append('cherry')
print(list1)

#to add element at a desired index syntax--> list.append(index no, element)
list1 = ['banana','papaya','apple']
list1.insert(1,'tomato')
print(list1)


#to remove an element from list syntax--> list.remove(element)
list1 = ['banana','papaya','apple']
list1.remove('banana')
print(list1)

#to remove all elements
#syntax --> list.clear()
list1 = ['banana','papaya','apple']
list1.clear()
print(list1)

#to get index number of element
#syntax--> list.index(element)
list1 = ['banana','papaya','apple']
print(list1.index('banana'))

#to get no of occurence of an element
list1 = ['banana','papaya','apple']
print(list1.count('banana'))

#to sort a list
list1 =[4,6,5,2,8,6,1]
list1.sort()
print(list1)

#to reverse a list
#syntax-->list.reverse()
list1 = ['banana','papaya','apple']
list1.reverse()
print(list1)

#to copy a list into a new list
list1 = ['banana','papaya','apple']
list2 = list1.copy()
print(list2)

#to remove the last element from list
#syntax--> list.pop()
list1 = ['banana','papaya','apple']
list1.pop()
print(list1)

#to remove an element by its index no
# syntax--> list.pop(index no)
list1 = ['banana','papaya','apple']
list1.pop(1)
print(list1)