#python code goes here
#python version :3 

n = int(input("Enter the number of elements :"))
k = int(input("Enter No. of rotations : "))
array = []
new_array = []
for i in range(n):
    array.append(int(input()))
while k>0:
    
    for i in range(n):
        new_array.append(array[i-1])
    for i in range(n):
        array[i] = new_array[i]
    new_array.clear()
    k=k-1;
print(array)
