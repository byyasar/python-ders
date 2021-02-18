'''a=3
b=5
print(a<3 and b>=5) 
print(a<3 or b>=5)   
print(not(a<3))'''

a=10
b=11
c=12
print (a is c)  #F
print (a is not b)#T
a+=1 #11
print (a is b) #T
a+=1 #12
print(a is c)#T