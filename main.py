age = int(input("How r u?"))

print("user answer", age)

print(type(age))

if age < 18:
    print("adolscent")
elif age >= 18 and age <= 35:
    print("In a gooooood time")
elif age == 60 or age == 70:
    print("...why still alive?")
else:
    print("adult")
