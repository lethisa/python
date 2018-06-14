# open and read file
# file = open("example.txt")
# content = file.read()

# file.seek(0)
# content = file.readlines()

#  content = [i.rstrip("\n") for i in content]
# append ==> file.write("example.txt", "a")

# read exaample.txt
file_1 = open("example.txt", "r")
content_1 = file_1.readlines()
file_1.close()
for i in content_1:
    print(len(i.strip()))

# read fruit.txt
file_2 = open("fruit.txt", "r")
content_2 = file_2.read()
file_2.close()
print(content_2)

# write to file
numbers = [1, 2, 3]
file = open("numbers.txt", "w")
for i in numbers:
     file.write(str(i) + "\n")
file.close()

# termometer
temperatures = [10, -20, -289, 100]

def writer(temperatures, filepath):
    with open(filepath, "w") as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9/5 + 32
                file.write(str(f)+"\n")
    
writer(temperatures, "temperature.txt")
