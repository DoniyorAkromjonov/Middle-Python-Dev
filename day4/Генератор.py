def my_gen():
    yield 1
    yield 2
    yield 3
    yield 4

for x in my_gen():
    print(x)

# 2 вариант
squares = (x * x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 2
print(next(squares))  # 3
print(next(squares))  # 4
print(next(squares))  # 5

