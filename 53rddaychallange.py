# dictionary =  a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "New York",
            "India": "New Delhi",
            "Japan": "Beijing"}
#vprint(capitals["India"])
# capitals.update({"Russia": "Moscow"})
#print(capitals)
# if capitals.get("Russia"):
#    print("The capital exists")
# else:
#    print("The capital doesn't exist")

# keys = capitals.keys()
# print(keys)

# for keys in capitals.keys():
#     print(keys, end= " ")

#values = capitals.values()
#print(values)

#for value in capitals.values():
#    print(value, end= " ")

for key, value in capitals.items():
    print(f" {key} : {value}")