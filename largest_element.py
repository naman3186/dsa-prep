arr=[12,34,10,10,23,89,32,45]
max=arr[0]

for i in arr:
    if i>max:
        max=i 

print(max)        


#second_largest
max=arr[0]
second_largest=-1
for i in arr:
    if i>max:
        second_largest=max 
        max=i

    if i>second_largest and i<max:
        second_largest=i 

print(second_largest)
