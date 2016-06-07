#python code goes here
#python version :3 
val = {'A':'Z', 'B': 'Y', 'C': 'Z', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}

def iso():
    str1 = str(input('Enter a string1: '));
    str2 = str(input('Enter a string1: '));
    str1 = str1.upper();
    str2 = str2.upper();
    a=len(str1);
    b=len(str2)
    if a==b:
        i=0;
        while i<a :
            f= val[str1[i]];
            d= val[str2[i]];
            if f==d:
                c=1;
            
            else:
                c=0;
                
            i=i+1;
           
    elif a!=b :
        c=0;
        return c;
    if c==1:
        print("the two strings are isomorphic");
    else:
        print("the two strings are not  isomorphic");
iso();
