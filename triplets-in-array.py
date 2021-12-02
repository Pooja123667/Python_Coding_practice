# triplets in a given array - sum of 2 numbers is equal to the third
# 2+3 = 5
# code needs to be optimized and improved
arr = [1, 5, 3, 2]
flag=False
def triplet(arr):
    n = len(arr)
    arr.sort() #sorting the array
    i=n-1
    while (i>=0):
        j=0
        k=i-1
        while (j < k):
            if (arr[i] == arr[j] + arr[k]):
               
                # pair found
                print("numbers are ", arr[i], arr[j], arr[k])
                return
            elif (arr[i] > arr[j] + arr[k]):
                j += 1
            else:
                k -= 1
        i -= 1
         
    # no such triplet is found in array
    print("No such triplet exists")
triplet(arr) 
