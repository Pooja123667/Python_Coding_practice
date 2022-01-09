# Return the 2nd occurence of the number given from a list of numbers
#using the index function to get the index of a certain number
num_list = [4,5,6,4,89,5]
get_pos_list = list() # to get all positions of that certain number 
num = 5
index_pos_list = []
index_pos = 0
while True:
    try:
        # Search for item in list from indexPos to the end of list
        index_pos = num_list.index(num, index_pos)
        # Add the index position in list
        get_pos_list.append(index_pos)
        index_pos += 1
    except ValueError as e:
        break

#print(get_pos_list)
if get_pos_list[1] == " ":
    print("0")
else:
    print (get_pos_list[1])
    
