set1 = set()
set2 = set()

for i in range(10):
    set1.add(i)

for i in range(5,2,-1): 
    set2.add(i)

set3 = set1.intersection(set2)

print("Intersection using intersection() function:")
print(set3)