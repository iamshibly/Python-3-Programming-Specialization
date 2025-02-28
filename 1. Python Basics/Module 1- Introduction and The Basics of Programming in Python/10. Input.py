#user input #user always string input dibe, amader nijeder convert korte hobe
n = input("Enter your age: ")
n=int(n)+1
print(n)

str_seconds= input("Enter seconds: ")
Hours = int(str_seconds) // 3600
Extra_Second = int(str_seconds) % 3600
Minutes = Extra_Second // 60
More_Extra_Second = Extra_Second % 60
Seconds = More_Extra_Second
print(Hours,"Hours",Minutes,"Minutes",Seconds,"Seconds")