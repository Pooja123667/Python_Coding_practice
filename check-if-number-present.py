def check_for_num(arr, X):
    n = len(arr)
    for j in range(n):
        if X == arr[j]
        return j
    return -1

t = int(input()) #number of test cases
for i in range(0,t):
    n = int(input()) #size of the array input
    arr = map(int,input().split())
    X = int(input())
    print(check_for_num(arr,X))
    
#can also use the arr.index() method to get the index printed, just pass the element as an argument
