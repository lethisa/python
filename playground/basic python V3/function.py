"""
learn function syntax in python
"""

# function definition
def minutes_to_hours(second, minutes=60):
    hours = minutes / 60 + second / 3600
    return hours

print(minutes_to_hours(300))

# function without any parameter
def say_hello():
    return "Hello"

# age function
def age_foo(age):
    new_age = float(age) + 10
    return new_age

age = input("input your age: ")
print(age_foo(age))

# fahrenheit to celcius function
def celciusToFahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celciusToFahrenheit(10))

# calculate length function
def stringLength(args):
    return len(args)

print(stringLength("Hai Dear"))
