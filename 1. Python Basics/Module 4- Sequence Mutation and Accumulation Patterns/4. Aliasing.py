#Aliased. Changes made with one alias affect the other.
a=[4,5,6]
b=[4,5,6]
print(a is b)
print(b is a)
b=a
print(a is b)
print(b is a)
print(a==b)
b[0]=3
print(b)
print(a)