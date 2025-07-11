name_list = ["Ayush", "John", "don"]
people = set(name_list)

print(people)

people.add("Alice")
print(people)
abc = people.union({"Robinhood", "Ayush","ayush"}) #duplication is not allowed 
print(abc)