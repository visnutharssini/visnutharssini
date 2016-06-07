val = {'A':' Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}

def ISOTRO():
    str1 = str(input('Enter a string1: '));
    str2 = str(input('Enter a string1: '));
    str1 = str1.upper();
    str2 = str2.upper();
   
    while str1&&str2!=0:
        for(i=0;i<len(str1);i++)
            str1[i]= val[str1[i]];
        for(i=0;i<len(2);i++)
            str2[i]= val[str2[i]];
           
    if str1==str2:
      print("the two strings are isomorphic");
    else:
       print("the two strings are not  isomorphic");
ISOTRO()       
