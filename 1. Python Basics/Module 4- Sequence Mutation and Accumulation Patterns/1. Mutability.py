fruits =["apple","orange","jackfruit","grape"]
print(fruits)
fruits[0]="banana"
fruits[2]="watermelon"
fruits[-1]="mango"
print(fruits)

ab = ['a','b','c','d','e']
print(ab)
ab[1:3]=['x','y']
print(ab)
ab[1:3]=[]
print(ab)
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)


#string
greetings="Hello word"
new_greetings= "J"+greetings[1:]
print(greetings)
print(new_greetings)

a="many moons"
b=a+" and many stars"
c=b+" litter"
d=c+" the night sky!"
e="M"+d[1:]
print(e)