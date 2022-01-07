# Cehck if prime or not numbers in a list
# once you infer that make separate lists of prime and non-prime numbers
# return a list within a list of prime and non-prime

soln_list = [] # defining a global list
prime_list = []
non_prime_list = []
flag=False
def number_lists(nums):
    for el in nums:
        if el == 1:
            pass
        else:
            for dig in range(2, el+1):
                if el%dig !=0: #tells its a prime number
                    flag = True
                    break
                else:
                    non_prime_list.append(el)
                    
                    
    if flag == True:
        prime_list.append(el)

    soln_list = [prime_list,non_prime_list]
                
    return soln_list
    
nums = [2,1,56,66,7]

print(number_lists(nums))
