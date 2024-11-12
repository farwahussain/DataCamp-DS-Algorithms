#Implement a binary search algorithm

def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1
    
    while first <= last:
        middle = int((first + last)/ 2)
        
        if search_value == ordered_list[middle]:
            return True
        
        elif search_value < ordered_list[middle]:
            last = middle - 1
            
        else:
            first = middle + 1
    
    return False


print(binary_search([2,5,8,13,15,16,18,19,21,25], 16))

print(binary_search([2,5,8,13,15,16,18,19,21,25], 14))