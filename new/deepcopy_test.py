import copy

l1=[1,2,3,4]
x=l1
y=copy.deepcopy(l1)
l1[1]="abc"
print(x)
print(y)
