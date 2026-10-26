def max_two(a, b):
    if a >= b:
        return a
    return b


num = int(input("Введите число: "))

if num % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")


n = int(input("Введите N: "))

if n <= 0:
    print("Ошибка: N должно быть больше нуля")
else:
    print(f"Числа от 1 до {n}, кратные 3:")
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i, end=" ")
    print()


print(f"max_two(3, 7) = {max_two(3, 7)}")
print(f"max_two(10, 2) = {max_two(10, 2)}")
print(f"max_two(5, 5) = {max_two(5, 5)}")