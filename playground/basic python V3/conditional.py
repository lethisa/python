# conditional
a = 5

if a < 5:
    print("less than 5")
elif a == 5:
    print("equal 5")
else:
    print("equal or greater than 5")

# age 
def yourAge(age):
    if age <= 17:
        print("teenager")
    elif age <=30:
        print("mature")
    else:
        print("say no")
    
age = int(input("input your age : "))
yourAge(age)
    
# string length
def stringLength(mystring):
    if type(mystring == int):
        return "sorry, integer don't have length"
    elif type(mystring == float):
        return "sorry, floats don't have length"
    else:
        return len(mystring)

# celcius to fahrenheit
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c*9/5+32
        return f

print(c_to_f(-273.4))
