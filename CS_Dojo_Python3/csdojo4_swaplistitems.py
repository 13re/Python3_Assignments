#swap list items 0 and 1. 

b = ["middle", "left", "right"]
temp = b[0] #assigning current value of index "0" to "temp". Temp is middle. 
b[0] = b[1] #assigning current value of index "1" to "0". 1 is now left. 
b[1] = temp #assigning current value of temp to b[1]. b[1] is now middle. 
print(b) 
#|
#| ___PRINTS___
#| ['left', 'middle', 'right']