phrase = "What a wonderful day to program"
tot=0
for char in phrase:
    if char != " ":
        tot=tot+1
print(tot)

s = "what if we went to the zoo"
x=0
for one in s:
    if one in ["a","e","i","o","u"]:
        x=x+1
print(x)
nums = [9, 3, 8, 11, 5, 29, 2]
maxNum=0
for fir in nums:
    if maxNum<fir:
        maxNum=fir
print(maxNum)

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for okay in words:
    if okay.endswith("e"):
        past_tense.append(okay+"d")
    else:
        past_tense.append(okay+"ed")
print(past_tense)

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words=0
for too in words:
    if len(too)>3:
        num_words+=1
print(num_words)


