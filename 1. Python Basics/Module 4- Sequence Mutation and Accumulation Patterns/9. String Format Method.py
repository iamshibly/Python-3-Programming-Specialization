name = "Rodney Dangerfield"
score = -1  # No respect!
print("Hello " + name + ". Your score is " + str(score))

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name=person[0]
    score=person[1]
    print("Hello "+name+". Your score is "+str(score))
    print("Hello {}. Your score is {}".format(name,score))

person=input("Enter Your Name: ")
okay="Hello {} !".format(person)
print(okay)
print("Hello {}!!".format(person))

originalPrice=float(input("Enter Original Price: "))
discountPercent=float(input("Enter Discount Percentage: "))
newPrice=originalPrice*(1-discountPercent/100)
print("{}tk discounted by {} is {}tk".format(originalPrice,discountPercent,newPrice))
print("{:.2f}tk discounted by {:.2f} is {:.2f}tk".format(originalPrice,discountPercent,newPrice))

name="Jhon"
status="I can not see you"
joss= "Hello,{},{}"
print(joss.format(name,status))
print(joss.format(status,name))
