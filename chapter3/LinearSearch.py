#Implement a linear search algorithm

def linear_search(unordered_list, search_value):
    #iterate over elements in a list
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True
    
    return False

print(linear_search([2,5,8,13,15,16,18,19,21,25], 16))