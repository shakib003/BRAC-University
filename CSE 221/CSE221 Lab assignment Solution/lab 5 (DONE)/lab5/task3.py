# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12HAiNdrKtXufHKoIZjxgHPVnVFihMMDJ
"""



#task 3
from queue import PriorityQueue

def dijakstra(dictt,s,n):
    onek_dure = 10000000000
    if(dictt=={}):
        return 1
    dist=[onek_dure]*(len(dictt)+1)
    dist[s]=0
    visited=[0]*(len(dictt)+1)
    
    q=PriorityQueue()
    
    prev=[0]*(len(dictt)+1)       
    
    for i in range(len(dictt[s][0])):
        q.put([dictt[s][1][i],dictt[s][0][i]])       
        dist[dictt[s][0][i]]=dictt[s][1][i]
        prev[dictt[s][0][i]]=s
    

    visited[s]=1                              
    
    while not q.empty():   
        u=q.get()

        if(visited[u[1]]==0):
            for i in range(len(dictt[u[1]][0])):
                c=u[0]
                c=c+dictt[u[1]][1][i]
                
                if(dist[dictt[u[1]][0][i]]>c and visited[u[1]]==0):
                    q.put([c,dictt[u[1]][0][i]])
                    dist[dictt[u[1]][0][i]]=c
                    prev[dictt[u[1]][0][i]]=u[1]       
        visited[u[1]]=1
    
    return prev


f=open("input3.txt","r")
file=open("output3.txt","w")

t=int(f.readline().strip())

while(t):
    dictt={}
    inputt=f.readline().strip().split()
    n=int(inputt[0])
    m=int(inputt[1])
    for i in range(m):
        count1=1
        count2=1
        temp=f.readline().strip().split()
        if(int(temp[0]) not in dictt):
            dictt[int(temp[0])]=[[int(temp[1])],[int(temp[2])]]
            count1=count1-1
        if(int(temp[1]) not in dictt):
            dictt[int(temp[1])]=[[int(temp[0])],[int(temp[2])]]
            count2=count2-1
        if(count1!=0):
            dictt[int(temp[0])][0].append(int(temp[1]))
            dictt[int(temp[0])][1].append(int(temp[2]))
        if(count2!=0):
            dictt[int(temp[1])][0].append(int(temp[0]))
            dictt[int(temp[1])][1].append(int(temp[2]))
     
    ans=dijakstra(dictt,1,n)
    array=[]
    if(ans==1):
        file.write(str(1)+"\n")
    else:
        temp=n
        array.append(temp)
        for i in range(len(ans)):
            if(ans[temp]==0):
                break
            else:
                array.append(ans[temp])
                temp=ans[temp]
            
 
        for i in range(len(array)):
            file.write(str(array.pop())+" ")
        file.write("\n")
    t=t-1;
file.close()