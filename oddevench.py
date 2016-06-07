#python code goes here
#python version :3 
a=str(input("enter the string"));
i=0;
b=len(a);
if(b%2==0):
    
    while i<b:
        t=a[i];
        s=a[i+1];
        print(s);
        print(t);
        i=i+2;
else:
    while i<b:
        t=a[i];
        s=a[i+1];
        print(s);
        print(t);
        i=i+2;
        if(i==b-1):
            f=a[i];
            print(f);
