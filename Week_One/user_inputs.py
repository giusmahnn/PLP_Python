def details():
    name = input("what is you name?")
    age = input("What is your age?")
    location = input("What is your location?")
    return f"Hello {name}, you are {age} years old and live in {location}"

print(details())
