# Compute all multiples of 3, 5
# that are less than 100. 

# print(list(range(1,100))) #checking to make sure the range function works 

#total = 0
#for eachnumber in range(1,100):
#        if (eachnumber % 3 == 0) or (eachnumber % 5 == 0):
#               print(eachnumber, end=" ") #figure out how to get all numbers on one line
#                total += eachnumber
#        if(eachnumber == 99):
#                print("") #adds enter-space
#print(total)

total = 0 #assign total as "0"
for eachnumber in range(1,100):
        if (eachnumber % 3 == 0) or (eachnumber % 5 == 9): 
        #if number is multiple of 3 or 5
                if (total==0): 
                #why 0? total will be "0" until we hit a multiple of 3 or 5
                #we get 3 because total is still "0"
                        print(eachnumber,end="")
                        total += eachnumber # 0 + 3 (so now total is 3)
                else:
                        print(",",eachnumber,end="")
                        total += eachnumber
print("") #adds enter-space
print(total)



#                 print(eachnumber, end=" ") #figure out how to get all numbers on one line


#Prints:
#| [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
#|  23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42
#|  , 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 6
#|  2, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 
#|  82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#| 2318

#Modulo Operator example:
#print(4 % 3) 
#divides 4 by 3 then prints the remainder: 1