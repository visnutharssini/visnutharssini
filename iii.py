arr=[];
count=0;
n=int(input("enter the no of elements"));
for i in range(n):
  arr.append(int(input()));
for i in range(n):
  if arr[i]==arr.index(a[i]):
     print(a[i],"this element value matches to the index value");
     count=count+1;
  else:
     count=count+0;
if count==0:
   print("no element matches");
