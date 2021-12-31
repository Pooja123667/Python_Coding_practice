# An array is  given, print all the even numbers before the odd

#basically i will iterate the entire array and swap if i get an odd element
lis = [12, 10, 9, 45, 2, 10, 10, 45]
print("Original list is", lis)
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        if lis[j]%2 == 0:
            # swapping code
            temp = lis[j]
            lis[j]=lis[i]
            lis[i]=temp
        
print("The new list is",lis)  
