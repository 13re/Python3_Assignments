a = [1, 2, -3]
print(a)
#|
#| ___PRINTS___
#| [1, 2, -3]


a.append(4) #adds (4) to the list "a"
print(a)
#|
#| ___PRINTS___
#| [1, 2, -3, 4]


a.append("words") #adds a string to the number list
print(a)
#| 
#| ___PRINTS___
#| [1, 2, -3, 4, 'words']


a.append([6, 7, 8]) #adds a list to a list
print(a)
#| 
#| ___PRINTS___
#| [1, 2, -3, 4, 'words', [6, 7, 8]]


a.pop() #deletes the last item of the list
print(a)
#| 
#| ___PRINTS___
#| [1, 2, -3, 4, 'words']

a[0] #retreives the item from list "a" with the index "0"
print(a[0]) #retreives the item from list "a" with the index "0"
print(a[3]) #retreives the 4th item which has the index "3" (because we count from "0")
#| 
#| ___PRINTS___
#| [1]
#| [4]

a[0] = 13 #assigns a new value (13) to the item from list "a" with index "0"
print(a[0]) 
#| 
#| ___PRINTS___
#| [13]

