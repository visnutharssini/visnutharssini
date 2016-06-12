arr=[];
 arr1=[];
 count=0;
 n=int(input("enter the number"));
 for i in range(n):
 	arr.append(int(input()));
 for i in range(n):	
      arr1.append(max(arr));
      arr.remove(max(arr));
    
 print(arr1);
 k=0;
 s=''
 for i in range(n):
 	print("returns:"arr1[i]);
 	
 print("order",arr1);
