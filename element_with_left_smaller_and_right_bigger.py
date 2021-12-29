# Element with left side smaller and right side greater
# all elements in left should be small , and all to the right should be greater



s = list(map(int, input().split(","))) #takes , separated numbers in one line input
siz = len(s)
final_list = list()
flag = "no"

for i in range(1, siz-1):
    cur = s[i]
    for j in range(0,i):
        if s[j] < cur:
            for k in range(i+1, len(s)):
                if s[k] > cur:
                    final_list.append(cur)
                    flag = "yes"
                    
if flag == "yes": print(set(final_list))
