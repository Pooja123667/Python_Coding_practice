# checking if the number is prime or not
prime = True # defining a flag
a = 7 # this is a prime number
for num in range(2,a):# we dont need 1 and the number itself since all will be divisible
    if a%num == 0:
        prime = False
    else:
        prime = True
if prime:
    print(a, 'is a prime number')
        
        
