
#question 1

# implement sequencial search (not binary as no sequence)
def sequencial_search(list, aim):
    for i in range(len(list)):
        if list[i] == aim:
            return i
    return -1

def determine(letter_s, letter_t):
    s_list = list(letter_s)
    t_list = list(letter_t)
    if len(s_list) != len(t_list):
        return False
    for i in range(len(s_list)-1):
        ans = sequencial_search(t_list, s_list[i])
        if ans == -1:
            return False
        s_list[i] = 0
        t_list[ans] = 0
    return True

#time complexity Big O: O(n**2)
#print(determine('angraam','nagaram'))

# Smarter answer:

def isAnagram(self, s, t):
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss==tt

#sort twice and compare

# or
    # return sorted(list(s)) == sorted(list(t))
#another better solution:

def isAnagram2(self,s,t):
    dict1 = {}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch,0) +1
    for ch in t:
        dict2[ch] = dict2.get(ch,0) +1
    return dict1 == dict2

#put in buckets and comapre (rather than sorting)

#question 2

#implement binary search as sequence exists
def binary_search(list, aim):
    left = 0
    right = len(list) -1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == aim:
            return mid
        elif list[mid] > aim:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def check_exist(twoD_list, aim):
    for i in range(len(twoD_list)):
        if aim >= twoD_list[i][0] and aim <= twoD_list[i][len(twoD_list[i])-1]:
            ans = binary_search(twoD_list[i], aim)
            if ans == -1:
                return "False"
            else:
                return "True"

B_list = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

# time complexity Big O: O(nlogn)
#print(check_exist(B_list, 50))

#shorter solution?: but slower

def searchMatrix(self, matrix, target):
    for line in matrix:
        if target in line:
            return True
    return False




#question 3

def combine_result(list,aim):
    append_list = []
    for i in range(len(list)):
        while list[i] > aim:
            i += 1
        if list[i] in append_list:
            return (list.index(aim-list[i]),i) #index() have tc of O(n).could be replaced by binary search
        # could set if statement determining from lefft or from right binary seach (only with sequence)
        append_list.append(aim-list[i])
    return "No pair satisfies the requirement"

# I could do
#   new_nums = [[num, i] for i, num in enumerate(nums)]  -> make a list[num,i] when num = enumerate(nums)[1]
#   and i = enumerate(nums)[0]
#   new_nums.sort(key = lambda x:x[0] ) -> sort items in list according to x[0] of "x items" of nums


#tc:O(n**2)

input_list = [1,2,5,4]
whole = 7

print(combine_result(input_list,whole))