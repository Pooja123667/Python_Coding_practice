# reversing an array in python
arr = [20,56,89]

# Method 1-Slicing
print(arr[::-1]) #new list of the reverse order rather than working on og list


# method 2 - using the reverse function
arr.reverse()
print(arr)

#using the for loop in reverse order
og_arr = [50,60,70]
new_arr = list()
for i in range(len(og_arr)-1,-1,-1):
    new_arr.append(og_arr[i])
print(" ".join(map(str,new_arr)))

    
