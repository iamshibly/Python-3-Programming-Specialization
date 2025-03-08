nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

w = range(10)

tot = 0
print("***** Before the For Loop ******")
for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)
print("***** End of For Loop *****")
print("Final total:", tot)
