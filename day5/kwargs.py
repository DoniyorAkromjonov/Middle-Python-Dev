def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value} ")

print_info(name="Alice", age=25)
print_info(name="Smone", age=23)
# name: Alice
# age: 25
