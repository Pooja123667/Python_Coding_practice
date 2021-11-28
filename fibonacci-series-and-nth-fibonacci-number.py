# python program for n-th fibonacci number
# using recursion
n = int(input("Enter the nth fibonacci number you would like to know: "))
def fibonacci(n):

    
    if n<=0:
        return "invalid input"
    if n==1:
        return 1
    if n==2:
        return 1
    else:


        return fibonacci(n-1) + fibonacci(n-2)
        
f1 = 0
f2 = 1
for x in range(1, n+1):
    print(f2, end=" ")
    next = f1 + f2
    f1 = f2
    f2 = next
print("\n\n","the",n,"th number is:",fibonacci(6)) #can be verified from the series
