# leaders in an array
# Given an array A of positive integers. Your task is to find the leaders in the
#array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

A = [16,17,4,3,5,2]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] <= A[j]:
            break #condition which is not favouravle
        if j == len(A)-1: #when the loop didnt break
            print(A[i])
print(A[-1]) #last element is a leader by default

