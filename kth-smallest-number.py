# find the kth smallest element given an unsorted element
arr = list(map(int, input().split(","))) #taking int array input
k = int(input("which number do u want: "))
print(arr)
arr = sorted(arr)
print(arr[k-1])
