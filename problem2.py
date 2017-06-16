# Problem 2
# Find the sum of all even termed fibonacci numbers less than 4 million
# First two numbers of the sequence are 1, 2

def fibonacci(a,b,max_fib):
    c = a + b
    if c < max_fib:
        fibonacci(b,c,max_fib)
    
    if (b % 2) == 0:
        global total
        total = b + total
        
    return total
        
total = 0
total = fibonacci(1,2,4000000)
print(total)
