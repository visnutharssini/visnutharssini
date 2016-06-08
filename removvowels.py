a=str(input("enter a string:"));
i=len(a)-1;
s='';
while(i>=0):
    s= s + str(a[i]);
    i=i-1;
print(s)
b="aeiou";
for char in b:
	s=s.replace(char,"");
print("after removing vowel");	
print(s)
