#Task 1: create an algorithm that prints all the elements of the given list
#Task 2: calculate big o notation

colors = ['green', 'yellow', 'blue', 'pink'] # n = 4

def linear(colors):
    for col in colors: # O(4) --> big O notation O(n)
        print(col)      
        
linear(colors)
 