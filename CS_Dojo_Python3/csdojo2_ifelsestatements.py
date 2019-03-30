# If Clause sample: 
small = 1
big = 100
if small < big:
    print("small is less than big")
    print("small is definitely less than big")
print("unsure if small is less than big")

# --------------------------------
print("") #adds extra line in print
# --------------------------------

quarter = 25
dollar = 100 
if quarter < dollar:
    print("quarter is less than dollar")
else: 
    print("quarter is not less than dollar")
    print("I don't think quarter is less than dollar")
print("outside the 'if' block")

# --------------------------------
print("") #adds extra line in print
# --------------------------------

quarter = 1
dollar = 4

if quarter < dollar: # 1st check
    print("quarter is less than dollar")
elif quarter == dollar: #2nd check / 2nd if to pass
    print("quarter is equal to dollar")
elif quarter > dollar + 10:
    print("quarter is greater than dollar by more than 10")
else: 
    print("quarter is greater than dollar")


# --------------------------------
print("") #adds extra line in print
# --------------------------------

g = 9
h = 8

if g < h:
    print("g is less than h")
else: 
    if g == h:
        print("g is equal  to h")
    else: 
        print("g is greater than h")