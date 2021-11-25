# reverse an integer in python

# method 1 ''' this method wont work if a digit zero is at the end''' 
num = 205 # you can define a user input here too
num = str(num)
print(num)
rev_num = num[::-1]
print(int(rev_num))


# method 2 - Accessing the digits from the integor
dig = 1000
num=dig
ls=list()
while num>0:
    dig=num%10
    print(dig)
    ls.append(dig)
    num=num//10
    print(num)

print(ls)
print("".join(map(str,ls))) #reversing done final output is a string 


# method 3 taking an empty string and appending the characters reversely 
numb = 456
res_num = ""
numb = str(numb)

for el in numb:
    res_num = el+res_num
    
    
print(int(res_num))

