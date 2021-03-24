# list mutables
a = [1, 2, "hola"]
print(a, id(a))
a[1] = "3"
print(a, id(a))
b = a.copy()
print("Este es el primer print de b: ", b, id(b))
a[2] = 3
b[2] = "Santiago"
print("Esta es la comparación de b y a: ", b, id(b), '\n', a)
print(len(b))
for a in range(len(b) - 1, -1, -1):
    print(b[a])

print(dir(b))

c = []

for i in range(0, 10):
    c.append(i)
print(c)
c.append(3)
# count how many items you have repeated in list
print(c, c.count("3"), c.count(3))
c.reverse()
# c.sort()
print(c.pop(3))
c.sort()
print(c)
# remove the first value equal to argument
# c.remove(3)
print(c)
# insert values in indicated position (position, value) if not position stack at the end of the list
c.insert(15, 100)
print(c)
# return position for value if we are going to use range (value, start, end)
print(c.index(3), "este es el index")
# clear all items
# c.clear()
print(c, "este es despues del clear")

c.extend([0, 1, 0, 1, 0, 2])
print(c + [0, 1, 0, 1, 0, 2], " este concatena igual que extend")
c.append(0)
print(c)

""" set  mutable """

a = set(c)
print("esteeeeedeee", a)
print(dir(a))
print(type(a), id(a))
a.add(1)

# for i in c:
# a.add(i)
# let to add a list in set
a.update(c, [500], (3005, 9000))
print(a.pop())
print(a.discard(3))
print(a)
print(a.remove(100))
print(a, id(a))
# for i in range(len(a)):
# print(a.pop())

# tuples unmutable
d = tuple(c)
print(d, id(d))
print(d[2])
print(dir(d), d.count(1))
print(d.index(100, 0, 15))
d = d + (0, 1)
print(d, id(d))

# Dictionary mutable
e = {"mundo": 1, "prueba": 2}
print(id(e), dir(e))
e["prueba"] = 100
print(id(e), e["prueba"])
for key, value in e.items():
    print(key, value)

""" ZIP """

a = [1, 2, 3]
b = ["a", "b", "c"]
c = ["hola", "mundo", "zip"]

d = zip(a, b, c)
print(list(d))