x=10
y=int(input("enter number: "))
if x>y:
    print(x,"is greater than",y)
elif 2*x==y:
    print(x,"is half of",y)
elif x<y:
    print(x,"is less than",y)
else:
    print(x,"is equal to",y)
#or , we can use another elif
# elif x==y
# print(x,"is equal to",y)
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if "false" in str1:
    output="False. You aren’t you?"
elif "true" in str1:
    output="True! You are you!"
    print(output)
else:
    output="Neither true nor false!"
