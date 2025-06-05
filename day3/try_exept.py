
try:
    x= 10/1
except ZeroDivisionError:
    print("Error")
else:
    print(x)
finally:
    print("Code end!")

# try:
# # код, который может вызвать ошибку
# except ТипОшибка:
# # что делать при ошибке
# else:
# # если ошибки не было
# finally:
# # выполняется всегда

