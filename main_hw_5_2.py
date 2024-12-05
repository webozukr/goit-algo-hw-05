# Домашнє завдання: Модуль - 5, завдання - 2. Python Core 2.0

"""Генератор generator_numbers здійснює пошук дійсних чисел в тексті.

Функція sum_profit - підраховує суму значень, повернутих генератором.

Спосіб використання:
text = (
    "Загальний дохід працівника складається з декількох частин: 1000.01 "
    "як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
"""
import re
from typing import Callable


# Генератор для пошуку дійсних чисел в тексті
def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\d+\.\d+'

    # Повернення знайдених чисел у форматі float з генератора
    for number in re.findall(pattern, text):
        yield float(number)


# Функція для підрахунку суми значень, що повертаються з генератора
def sum_profit(text: str, func: Callable) -> float:
    # Виклик генератора, знаходження суми та повернення загального результату
    return sum(func(text))
