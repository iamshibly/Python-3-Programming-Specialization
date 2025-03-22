a=[8,9,10]
b=a[:]#clone of a in b by using empty slicing
print(a)
print(b)
print(a is b)
print(a==b)
b[0]=11
print(b)
print(a)