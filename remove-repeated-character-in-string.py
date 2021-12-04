
# remove the repeated character in string
in_string = input("Enter the string you want to check: ")
count = 0



if len(in_string) == 0 or len(in_string) == 1:
    print(in_string)
else:
    for i in range(len(in_string)-1): #will go upto 4 --> 0,1,2,3
        if in_string[i] == in_string[i+1]:
            print("yes") 
            f_string = in_string.replace(in_string[i],"")
            count = count + 1
        else:
            print("no repetition")
    print(f_string)
    print("The number of times deletions required in string", count)
