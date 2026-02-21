def caching_fibonacci():
    # Створюємо кеш для збереження обчислених значень
    cache = {}

    def fibonacci(n):
        # Базові випадки рекурсії
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Якщо значення вже є в кеші — повертаємо його
        if n in cache:
            return cache[n]

        # Обчислюємо та зберігаємо результат у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повертаємо обчислене значення
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610