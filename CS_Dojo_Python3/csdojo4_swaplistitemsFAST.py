#swap list items 0 and 1. 

b = ["middle", "left", "right"]
b[0], b[1] = b[1], b[0] #swaps the two variables at the same time. 
print(b) 
#|
#| ___PRINTS___
#| ['left', 'middle', 'right']