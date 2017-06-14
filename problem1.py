# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

multiple = 1000
a = 3
b = 5
multiple_list = []

i = 1

while (a*i) < multiple:
    if (b*i < multiple) and (b*i not in multiple_list):
        multiple_list.append(b*i)
        
    if (a*i < multiple) and (a*i not in multiple_list):
        multiple_list.append(a*i)
          
    i += 1
    
print(multiple_list)

# Compute sum of list content
total = 0
for i in multiple_list:
    total = total + i

print(total)