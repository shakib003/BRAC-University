# -*- coding: utf-8 -*-
"""task3(ii)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sxsty7lpUCtMEKeB38MEprSSRj-iJen4
"""



#task 3(ii)

def partition(array,start,end):   
    pindex=start;
    pivot=int(array[end]);
    for i in range(start,end):
        if(int(array[i])<=pivot):
            array[i],array[pindex]=array[pindex],array[i];
            pindex+=1;
    array[pindex],array[end]=array[end],array[pindex]
    return pindex;

def findK(array,start,end,k):
    if(start<=end):
        pindex=partition(array,start,end);
        if(pindex==k):                                                                   
            file1.write(array[pindex]+"\n")                            
        elif(pindex<k):
            findK(array,pindex+1,end,k);
        elif(pindex>k):
            findK(array,start,pindex-1,k);

f=open("input3ii.txt",mode="r");
file1=open("output3ii.txt",mode="w");
array=f.readline().strip().split(":")
array=''.join(array[1])
array=array.split()
start=0;
end=len(array)-1;
for i in range(3):
    temp=f.readline().strip().split('=')
    k=int(temp[1])-1
    findK(array,start,end,k)
    
file1.close()