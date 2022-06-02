
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [4, 7, 5, 2, 6, 8, 10, 9, 3, 1]
c = [2, 4, 5, 7, 1, 3, 6, 8]

def sequencial_search(list, aim):
    for i in range(len(list)):
        if list[i] == aim:
            return i
    return "No this value"

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
    return "No this value"

def bubble_sortion(list):
    for i in range(len(list) - 1):
        for j in range (len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

def selection_sortion(list):
    for i in range(len(list)-1):
        k = i
        for j in range(i+1, len(list)):
            if list[k] > list[j]:
                k = j
        list[i],list[k] = list[k], list[i]

def insertion_sortion(list):
    for i in range(1,len(list)): #index of touched card
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j-=1
        list[j+1]= temp

def partition(list, left, right):
    temp = list[left]
    while left < right:
        while left < right and temp <= list[right]:
            right -=1
        list[left] = list[right]
        while left < right and temp >= list[left]:
            left += 1
        list[right] = list[left]
    list[left] = temp
    return left

def quick_sortion(list, left, right):
    if left<right:
        mid = partition(list, left, right)
        quick_sortion(list, left, mid -1)
        quick_sortion(list, mid+1, right)

def sift(list, low, high):
    '''

    :param list: input list
    :param low: the root node
    :param high: the last element of the heap
    :return: no return
    '''
    i = low
    j = (2*i)+ 1
    temp = list[low]
    while j <= high:
        if j+1 <= high and list[j+1] > list[j]: #left: have right | right: right>left
            j = j+1
        if temp < list[j]:
            list[i] = list[j]
            i = j
            j = (2*i) + 1
        else:
            list[i] = temp
            break
    else:
        list[i] = temp

def heap_sortion(list):
    n = len(list)
    for i in range((n-2)//2, -1 , -1):
        sift(list, i, n-1)
    for i in range(n-1, -1, -1):
        list[0], list[i] = list[i], list[0]
        sift(list, 0, i-1)

import heapq

def heapq_sortion(list): #print
    n = len(list)
    heapq.heapify(list)
    for i in range(n):
        print(heapq.heappop(list),end=' ')


def merge(list, low, mid, high):
    i = low
    j = mid+1
    ltemp = []
    while i <= mid and j <= high:
        if list[i] < list[j]:
            ltemp.append(list[i])
            i +=1
        else:
            ltemp.append(list[j])
            j+=1
    while i <= mid:
        ltemp.append(list[i])
        i += 1
    while j <= high:
        ltemp.append(list[j])
        j += 1
    list[low:high+1] = ltemp

from cal_time import*



def merge_sort(list, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(list,low,mid)
        merge_sort(list,mid+1,high)
        merge(list,low,mid,high)





#for random list:

import random
z = list(range(1000000))
random.shuffle(z)



#@cal_time
def tester2(list,low,high):
    a = list
    merge_sort(a, low, high)
    return 1

#@cal_time
def tester1(list,low,high):
    a  = list
    a.sort()
    return 1

#print(z)
#print(tester1(z,0,len(z)-1))
#print(tester2(z,0,len(z)-1))

#heapq_sortion(b)
#print(b)







