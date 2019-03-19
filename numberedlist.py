# write a function that takes a list as an argument 
# and prints out all the values in the list along with the index
# Example: [apple, banana, organge]
# #1 is apple
# #2 is banana
# then try:
# 1st element in the list is apple
# 2nd element in the list is banana

#need to print the list with #in front + [i]

meals = ["breakfast", "lunch", "dinner", "dessert"]
listlength = len(meals)
i = 0
while i < listlength:
    a = i
    i = i+1 #counter 
    print("#",i,"meal is", meals[a])
