#strings slicing
singers = "Peter, Paul, and Mary"
print(len(singers))
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])
print(singers[5:])
print(singers[:7])
print(singers[:])
print(len(singers[:8]))

#list slicing
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])
a_list = a_list[1:3] +["good",5,6]+ a_list[4:5]
print(a_list)

#tuples Slicing
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)
L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-2]))
print(L[1:-2])