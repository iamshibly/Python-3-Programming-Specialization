orglist=["abc",5,7]
orglist.append("cat")
print(orglist)

#concatenate
orglist=["a",5,6]
orglist=orglist+["cat"]
print(orglist)

orglist=[3,4,5]
print(orglist)
print(id(orglist))
newlist=orglist+["cat"]
print(newlist)
print(id(newlist))

s="shibly"
p=[]
q=p+[s[0]]
r=q+[s[1]]
t=r+[s[2]]
u=t+[s[3]]
v=u+[s[4]]
w=v+[s[5]]
print(w)

a=[]
a.append(s[0])
a.append(s[1])
a.append(s[2])
a.append(s[3])
a.append(s[4])
a.append(s[5])
print(a)


