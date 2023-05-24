# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JDXGpMv6_oosCSfzWjQRG4pkVRImrSZk
"""

#task3
f1 = open("input3.txt","r")
r1 = f1.readline()
f2 = open("output3.txt","w")
for line in f1:
  l = line.split(" ")
for i in range(len(l)):
  l[i]=int(l[i])
for j in range(len(l)):
  count = 0
  for i in range(len(l)-1-j):
    if l[i]>l[i+1]:
      temp = l[i+1]
      l[i+1] = l[i]
      l[i] = temp
      count+=1
  if count==0:
    break
print(l)
for i in range(len(l)):
  f2.writelines(str(l[i])+' ')
f1.close()

#Here I have taken a swipe counter. In the outer for loop's 1st iteration the 
#inner for loop runs "n" times, which means it tries to swipe the value if it
#is bigger then it's right side's value. Now if the couter remains zero after the inner
#for loop running "n" times, that means no swipe was done, which means the order 
#was already in the right order in the first place(best case).
#So I terminated the outer for loop if it findes the counter==0 after 1st iteraton
#In this way the time complexity becomes theta(n) for the best case.