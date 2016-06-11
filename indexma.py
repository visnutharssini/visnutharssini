arr=[];
count=0;
n=int(input("enter the number"));
for i in range(n):
	arr.append(int(input()));
for i in range(n):	
	if arr[i]==arr.index(arr[i]):
		print(arr[i],"the element matched to its index value");
		count=count+1;
	else:
		count=count+0;
if count==0:
	print("not match")
