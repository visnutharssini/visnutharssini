num = int(input("Enter the number : "))
k = x = num
sum = 0;
def split(x):
    new_array = []
    while(x>0):
        new_array.append(x%10)
        x = int(x/10)
    return new_array
new_array = split(x);
for i in range(len(new_array)):
    sum += new_array[i]**2
    k = sum;
       
if(k == 1):
    print("%d is a Happy Number" % num);
else:
    print("%d is not a Happy Number"%num);
               
