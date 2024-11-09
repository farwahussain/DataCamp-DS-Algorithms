#create a recursive implementation of an algorithm that generates the sequence of Fibonacci sequence, which is ubiquitous in nature. 
#The first numbers are 0 and 1, and the rest are the sum of the two preceding numbers.

#Step 1: code Fibonacci using recursion.
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    
print(Fibonacci(6))

#step 2: improve it by using dynamic programming, saving the solutions of the subproblems in the cache variable.

cache = [None]*(100)
def fibonacci(n):
    if n <= 1:
        return n
    if not cache[n]:
        cache[n] = fibonacci(n - 1) + fibonacci(n -2)
    return cache[n]


print(fibonacci(6))