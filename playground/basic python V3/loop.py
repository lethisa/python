# for loop
emails = ["anda@gamail.com", "budi@yahoo.com","ita@gmail.com"]
for item in emails:
    if "gmail" in item:
        print(item)

# for loop blockthat iterates
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    if i > 2:
        print(i)

# while loop
password = ""
while password != "python":
    password = input("enter password : ")
    if password == "python":
        print("success login")
    else:
        print("try again")

# while loop multiple list
names = ["jame", "john", "jack"]
email_domains= ["gmail", "hotmail", "yahoo"] 

for a,b in zip(names,email_domains):
    print(a,b)

# termometer
def c_to_f(c):
    if c < -275.15:
        return "that temperature doesn't make sense"
    else:
        f = c * 9/5 + 32
        return f

temperatures = [10, -20, -289, 100]
for item in temperatures:
    print(c_to_f(item))


