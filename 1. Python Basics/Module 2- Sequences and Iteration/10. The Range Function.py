print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

 #Notice the casting of `range` to the `list`
print("range(1,10,2): ")
for i in range(1,10, 2):#2 is step
    print(i)
print("range(0,11,2)")
for i in range(0,11,2):
    print(i)

for i in list(range(3)):
    print(i)

accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)

nums=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in nums:
    count=count+1
print(count)