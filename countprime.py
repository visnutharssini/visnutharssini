a=int(input("enter the lowest range"));
b=int(input("enter the highest range"));
for i in range(a,b):
    count1=0;
    count2=0;
    if i%2==0:
        count1=count1+1;
        
    else:
        count2=count2+1;
        
print("no of prime number in given range:",count2);    
