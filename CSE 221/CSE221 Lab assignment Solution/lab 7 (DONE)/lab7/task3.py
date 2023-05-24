# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XhJWWQBXSeWvNBsxrLF-HQepJO6mvvYB
"""



#task3

def LCS(a,b):

  array=[]
  for i in range(len(a)+1):
    array1=[]
    for j in range(len(b)+1):
        array1.append(0)
    array.append(array1)
    
  for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
      if(a[i-1]==b[j-1]):
        array[i][j]=array[i-1][j-1]+1
            
      else:
        if(array[i-1][j]>array[i][j-1]):
          array[i][j]=array[i-1][j]
        else:
          array[i][j]=array[i][j-1]
                    
  i=len(a)
  j=len(b)
    
  c=""
    
  while(i>0 and j>0):
        
    if(array[i][j]==array[i-1][j]):
      i=i-1
        
    elif(array[i][j]==array[i][j-1]):
      j=j-1
            
    else:
            
      c=c+a[i-1]
            
      i=i-1
      j=j-1
            
  return c[::-1]

input = open("input3.txt","r")
output = open("output3.txt","w")

a = input.readline()
a = a.strip()
b = input.readline()
b = b.strip()
c = input.readline()
c = c.strip()

d = LCS(a,b)
e = LCS(d,c)
output.writelines(str(len(e)))