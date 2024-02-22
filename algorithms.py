from array import array
# 1st algorithm : Linar search method
def linear_search (my_array, target):
    #cnt = 0
    for i in range(len(my_array)):
        #cnt +=1
        if my_array[i] == target:
            return i
    return -1  
#print("Target not found #1 " + str(cnt))

#2nd algorithm : Binary search method

def binary_search (my_array, target):
    #my_array = array('i',sorted(my_array))
    #cnt = 0 
    min = 0
    max = len(my_array)-1
    while min <= max :
        #cnt += 1
        mid = (min + max) // 2
        if my_array[mid] == target:
            return mid
        elif my_array[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    return -1 
#print("Target not found #2 " + str(cnt))


'''
def binary_search_reverse (array, target):
    rev_array = sorted(array, reverse=True)
    min = 0
    max = len(rev_array)-1
    while min <= max :
        mid = (min + max) // 2
        if rev_array[mid] == target:
            return mid
        elif rev_array[mid] < target:
            max = mid - 1
        else:
            min = mid + 1
    return print("Target not found")

'''

#3rd algorithm : Ternary search method

def ternary_search (my_array, target):
    #my_array = array('i',sorted(my_array)) 
    low = 0
    high = len(my_array) - 1 
    #cnt = 0
    while low <= high : 
        #cnt += 1
        mid1 = low + (high-low) // 3
        mid2 = high - (high-low) // 3
        if my_array[mid1] == target:
            return mid1
        elif my_array[mid2] == target:
            return mid2
        elif my_array[mid2] < target :
            low = mid2 + 1 
        elif my_array[mid1] > target :
            high = mid1 - 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1 
#print("Target not found #3  " + str(cnt))

'''

def ternary_search_reverse (array, target): 
    rev_array = sorted(array, reverse=True)
    low = 0
    high = len(rev_array) - 1 

    while low <= high : 
        mid1 = low + (high-low) // 3
        mid2 = high - (high-low) // 3
        if rev_array[mid1] == target:
            return mid1
        elif rev_array[mid2] == target:
            return mid2
        elif rev_array[mid2] > target :
            low = mid2 + 1 
        elif rev_array[mid1] < target :
            high = mid1 - 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return print ("Target not found")


#array = [2,4,8,6,12,10,25,30,20]
#print(ternary_search_reverse (array, 25))
#print(ternary_search(array,4))

'''