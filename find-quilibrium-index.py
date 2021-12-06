# find the equilibrium point in the array
s = [1,3,5,2,2]
# sum before = sum after that element is the same 
def eq(s):
    left_sum = 0
    right_sum = 0
    n = len(s)
    
    for i in range(n):
        left_sum = 0
        right_sum = 0
        
        # get left sum
        for j in range(i):
            left_sum += s[j]
        
        for j in range(i+1,n):
            right_sum +=s[j]
            
        if left_sum == right_sum:
            return i
            
    return -1

print(eq(s)) # gets the index of the equilibriumposition
