nums = [1, 2, 3]

# Интератор
for n in nums:
    print(n)

# что происходит внутри
it = iter(nums)  # превращает список в итератор
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

