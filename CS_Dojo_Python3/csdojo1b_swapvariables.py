# How can you swap the values within these two variables? 

v1 = "last"
v2 = "first"

# ------------------------------------

#could do this, but it would be combersome:
#with longer strings to re-write. 
# v1 = "first"
# v2 = "last"

# --------------------------------------

# Name Swap (non-working solution)
# v1 = v2 # "v1" now refers to "first"
# v2 = v1 # "v2" would still refer to "first"
# therefore the variables are not swapped. 

# ---------------------------------------

# 2 Temp Variable (working solution)

b1 = "4th"
b2 = "3rd"

temp1 = b1 # temp variable to refer current value of "b1": "last"
temp2 = b2 # temp variable to refer current value of "b2": "first"

b1 = temp2 # b1 now refers to "first"
b2 = temp1 # b2 now refers to "last" 

print(b1, b2)

# ---------------------------------------

# 1 Temp Variable (working solution)

temp = v1 
#temp holds the value that v1 currently refers to

v1 = v2 # v1 now refers to v2
v2 = temp # v2 now refers to temp
# temp still holds the old value of v1,
# so the variables are now swapped. 

print(v1)
print(v2)

# ---------------------------------------

#The quickest way to swap in Python is using Tuples. Ex: 

a1 = "2nd"
a2 = "1st"

a1, a2 = a2, a1

print(a1, a2)