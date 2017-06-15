# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

multiple = 1000
a = 3
b = 5
multiple_list = []

i = 1

def sum_multiple(multiple, a, b):
    multiple_list = []
    i = 1
    
    while (a*i) < multiple:
        if (b*i < multiple) and (b*i not in multiple_list):
            multiple_list.append(b*i)
            
        if (a*i < multiple) and (a*i not in multiple_list):
            multiple_list.append(a*i)
              
        i += 1
    
    
    # Compute sum of list content
    total = 0
    for i in multiple_list:
        total = total + i
    
    print(f"The sum of all multiples of {a} or {b} less than {multiple} is: {total}") 
    
sum_multiple(1000, 3, 5)