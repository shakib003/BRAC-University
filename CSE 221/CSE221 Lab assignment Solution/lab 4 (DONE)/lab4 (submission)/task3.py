# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17u7k0COffjR8fvGgv5qNvu1BUrmaHct3
"""



#Task-3


f = open("/content/input3_3.txt", "r")
output=open("/content/output3_3.txt","w")
line = f.readline()
a,b = line.split(" ")
b = b.strip()
b = int(b)
a = int(a)
listgraph = [[]]*a
list1 = []
c = 0
while(c<b):
  list2 = []
  line = f.readline()
  d,e = line.split(" ")
  e = e.strip()
  e = int(e)
  d = int(d)
  if d in list1:
    listgraph[d-1].append(e)

  else:
    list1.append(d)
    list2.append(e)
    listgraph[d-1] = list2
  c+=1


graph = listgraph
#print(graph)

visited = [1]
  
Stack = [1]
while Stack:
  deStack = Stack.pop()
  output.writelines(str(deStack))
  output.writelines(" ")
  for i in graph[deStack-1]:
    if i not in visited:
      visited.append(i)
      Stack.append(i)