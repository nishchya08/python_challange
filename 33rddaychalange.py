# Traditional way

data = {}
items= [('a', 1), ('b', 2), ('a', 3)]
for key, value in items:
    if key not  in data:
        data[key] = []
    data[key].append(value)

# Genius way

data= {}
for key, value in items:
    data.setdefault(key, []).append(value)
print(data)