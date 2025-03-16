list1 = [99, 8, 25, 63, 70, 28]
last2=[]
for insert in list1:
    if insert>90:
        last2.append("A+")
    elif insert>70:
        last2.append("B+")
    elif insert>50:
        last2.append("C+")
    elif insert>20:
        last2.append("D+")
    elif insert>0:
        last2.append("Fail")
print(last2)

