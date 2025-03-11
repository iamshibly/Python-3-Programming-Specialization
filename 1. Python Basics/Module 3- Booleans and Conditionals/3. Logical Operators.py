x = True
y = False
print(x and y)
print(x or y)
print(not x)
x = 5
print(x>0 and x<10)
n = 25
print(n%2==0 or n%3==0)

total_batsman = int(input("enter number"))
total_run = int(input("enter score"))
probavg = int(input("enter avg"))
if total_run/total_batsman > probavg:
    print("Good game")
else:
    print("Bad game")