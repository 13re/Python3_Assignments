a = ["one", "two", "three"]
print(a[0])
print(a[1])
print(a[2])
#^ cumbersome way of iterating through lists, 
# especially if list had over 100 items.
#|
#| ___PRINTS___
#| one
#| two
#| three


for element in a:
    print(element) 
#for loop example prints same as above
#*the word "element" can be replaced by any other text, ex: "c"
#|
#| ___PRINTS___
#| one
#| two
#| three


for element in a:
    print(element)
    print(element) 
#^^for loop example that print each item twice
#|
#| ___PRINTS___
#| one
#| one
#| two
#| two
#| three
#| three


b = [1, 10, 100] 
total = 0
for e in b: 
    total = total + e 
    #assigns the old value of "total" + "e" to the new value of "total"
    #adds each element "e" to total
    #"e" will be 1, then 10, then 100
print(total) #finds the sum of the list


#find the sum of 1, 2, 3, 4
#use the range function
range(1,5)
#means the range of 1-5 but not including 5
#like a list

d = list(range(1,5)) #makes it a list using list function
#convert to a list to see what's inside
print(d) 

for rangevalue in range(1,5):
    print(rangevalue)

total2=0
for rangevalue in range(1,5):
    total2 += rangevalue 
    #the new value of "total2" should equal 
    # the old value of "total2" + "rangevalue"
    print(total2)

range(1,8) #range of 1-8, but not including 8

print(list(range(1,8)))
#prints: [1, 2, 3, 4, 5, 6, 7]
#now add all the multiples of 3
total3 = 0
for i in range(1,8):
    if i % 3 == 0: 
        #if true then 
        #if i mod 3 = 0 then...
        #to check if muliple of 3, use modulo operator
        total3 += i
print(total3) # 3 + 6 = 9
# prints: 9


#Modulo Operator example:
print(4 % 3) 
#divides 4 by 3 then prints the remainder: 1

