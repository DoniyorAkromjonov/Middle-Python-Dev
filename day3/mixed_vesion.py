try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found! Write files name correct!")
else:
    print(content)
finally:
    print("End")
