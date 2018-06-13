#variable
A = "Hello"
B = "World !"
print(A)
print(B)

# input
msg = input("say something : ")
print(msg)

# number - use type() to verify type
_a = 1
_b = 2
print(_a + _b)

age = input("enter your age: ")
new_age = int(age) + 10
print(new_age)

# dir(content)
_contes = "sample text"
print(_contes)
# heelp("".replace)
new_contes = _contes.replace("a", "i", 1)
print(new_contes)

# string indexing and splitting
a = "Hai There!"
print(a[3]) 
print(a[0:2])
print(a[:3])
print(a[3:-1])

# list - support any type
listed = ["H", 2, "Hello"]
print(listed[1])
print(listed[0:2])
print(type(listed[0:2]))

# tuples - not mutate
t = ("Hello", 3, 4)
print(t)
print(type(t))

# dictionaries - key value
d = {"name":"lethisa","age":21}
print(d["name"])
print(type(d))