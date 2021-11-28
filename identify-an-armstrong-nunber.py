# program to check armstrong number
# numbber is equal to the sum of cubes of its own digits
# eg. 370 = 3*3*3 (27) + 7*7*7 (343) + 0*0*0 (0) = 370
num = 370 # you can give an input accordingly
n = num
dig_cube_ls = list() # this list will stor4e the cubes of the digits of the number

while n!=0:
    dig = n%10
    dig_cube_ls.append(dig**3) #appending the cubes of the digits in list above
    n = n//10
    
s = sum(dig_cube_ls)
print(s)
if s == num:
    print("Number is an armstrong number")
else:
    print("not armstrong")
