#implement the binary search algorithm using recursion

def BS_recursive(ordered_list, search_value):
    #set base case
    if len(ordered_list) == 0:
        return False
    
    else:
        middle = len(ordered_list)//2
        
        if search_value == ordered_list[middle]:
            return True
        
        elif search_value < ordered_list[middle]:
            #recall function for first sub-list
            return BS_recursive(ordered_list[:middle], search_value)
        
        else:
            #recall function for second sub-list
            return BS_recursive(ordered_list[middle +1 :], search_value)
        

print(BS_recursive([2,5,8,13,15,16,18,19,21,25], 16))