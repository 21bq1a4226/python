names={}
n=int(input("enter number of names:"))
for i in range(2):
    names[i+1]=input("enter a name:")
name=list(names.values())
pos=int(input("enter position:"))
name.sort(key=lambda x:x[pos])
print(name)