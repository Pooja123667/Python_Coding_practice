#setting the upper limit as 15 here - Can be a user input as well

def pythagorean_triplets(limits) :
   c, m = 0, 2
   while c < limits :
   for n in range(1, m) :
      a = m * m - n * n
      b = 2 * m * n
      c = m * m + n * n
      if c > limits :
         break
      print(a, b, c)
   m = m + 1
upper_limit = 15
print("The upper limit is :")
print(upper_limit)
print("The Pythagorean triplets are :")
pythagorean_triplets(upper_limit)





# Simpler approach can be optimized
# Basic coding question
A = [3, 2, 4, 6, 5]
#since triplets, we need 3 for loops to iterate

for i in A:
    for j in A:
        for k in A:
            if (i**2 + j**2 == k**2): 
                print("The triplets are - ", i,j,k)
