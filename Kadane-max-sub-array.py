#KADANE'S ALGORITHM - MAX CONTIGOUS SUM
#step 1 - first find the maximum sum the array cane have
#step 2 - Now, find the window in which the max sum occurs/comes
def max_subarray(arr):
    size = len(arr)
    cur_sum = 0 # initiating current sum as zero
    max_so_far = arr[0]
    st=0 # start index
    en=0 # end index
    poi = 0 #tenporary pointer
    for i in range(size):
        cur_sum = cur_sum + arr[i]
        if max_so_far < cur_sum:
            max_so_far = cur_sum
            st = poi
            en = i
        if cur_sum<0: #for negative number condition since we want to compare with 0
            cur_sum = 0
            poi=i+1
    print("maximum sum so far", max_so_far)
    print("array window we get is", arr[st:en+1])

max_subarray([1, 2, 3, -2, 5])
    
    
