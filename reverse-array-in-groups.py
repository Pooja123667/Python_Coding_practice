# reverse array in groups
A = [1,2,3,5,45,6]
k = int(input("Enter sub-array group size: "))

    
# number of groups will be len(A)/k in this case 2  
def reverse_group(A,k):
    start = 0
    result = []
    while (start<len(A)):
  
           # if length of group is less than k
           # that means we are left with only last 
           # group reverse remaining elements 
           if len(A[start:])<k:
                result = result + list(reversed(A[start:]))
                break
  
           # select current group of size of k
           # reverse it and concatenate 
           result = result + list(reversed(A[start:start + k]))
           start = start + k
    print(result)
    
reverse_group(A,k)
    
    
