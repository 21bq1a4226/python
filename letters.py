words=["Arun","Varun","Kent","Eat","Toe","Pot","Peak","Net","Peacock","Zebra","Nato","Poke","Knife","Poet","Venus","Ant"]
list=['A','K','E','O','T','P','N']
res=[]
for x in words:
    count=0
    for l in list:
        if l in x.upper():
            count+=1
            if count==len(x):
                res.append(x)
print("words formedfrom given letters are:\n",res)