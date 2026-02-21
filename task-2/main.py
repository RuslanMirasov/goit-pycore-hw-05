import re
from typing import Callable

# Генеруємо всі дійсні числа з тексту (включно з від'ємними).
def generator_numbers(text: str):
    pattern = r"-?\d+(?:\.\d+)?"

    for number in re.findall(pattern, text):
        yield float(number)

# Обчислюємо загальну суму чисел.
def sum_profit(text: str, func: Callable):
    total = 0

    for number in func(text):
        total += number

    return total

# Приклади використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
text_with_negative_numbers = "Загальний дохід 1000 доларів + премія 100 та сплата штрафу -50 доларів. Податки 0 доларів"

total_income = sum_profit(text, generator_numbers)
total_income_with_negative_numbers = sum_profit(text_with_negative_numbers, generator_numbers)

print(f"Загальний дохід: {total_income}")
print(f"Загальний дохід: {total_income_with_negative_numbers}")