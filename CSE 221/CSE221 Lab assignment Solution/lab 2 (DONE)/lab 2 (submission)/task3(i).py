# -*- coding: utf-8 -*-
"""task3(i)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wu5RgEYZ4d2PhpB0sIAEVcUQIjeS8g6l
"""



#task 3(i)

def partition(array,start,end):
    pivot=int(array[end])
    pindex=start
    for i in range(start,end):
        if(int(array[i])<=pivot):
            array[i],array[pindex]=array[pindex],array[i]
            pindex=pindex+1;
    array[pindex],array[end]=array[end],array[pindex]
    return pindex;


def quicksort(array,start,end):
    if(start<end):
        pindex=partition(array,start,end)
        quicksort(array,start,pindex-1)
        quicksort(array,pindex+1,end)

f=open("input2.txt","r")
file1=open("output3i.txt","w")
for i in range(2):
    array=f.readline().strip().split();
    array2=array[:]
    quicksort(array,0,len(array)-1)
file1.write(str(' '.join(array))+"\n")
file1.close()