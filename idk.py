def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime_numbers = []


n = int(input("Введите количество чисел для проверки: "))


for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    if is_prime(num):
        prime_numbers.append(num)

print("Простые числа:", prime_numbers)
