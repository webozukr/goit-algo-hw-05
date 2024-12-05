# Домашнє завдання: Модуль - 5, завдання - 4. Python Core 2.0. (PYTHON SOFTWARE ENGINEERING. Гнучкий формат)
'''
ОПИС:
    Скрипт, який є консольним ботом-помічник, який розпізнає команди,
    що вводяться з клавіатури, та відповідає відповідно до введеної команди.
ВХІДНІ КОМАНДИ ТА ВИВІД:
    1. Команда "hello":
        Введення: "hello"
        Вивід: "How can I help you?"
    2. Команда "add [ім'я] [номер телефону]":
        Введення: "add John 1234567890"
        Вивід: "Contact added."
    3. Команда "change [ім'я] [новий номер телефону]":
        Введення: "change John 0987654321"
        Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
    4. Команда "phone [ім'я]":
        Введення: "phone John"
        Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
    5. Команда "all":
        Введення: "all"
        Вивід: усі збережені контакти з номерами телефонів
    6. Команда "close" або "exit":
        Введення: будь-яке з цих слів
        Вивід: "Good bye!" та завершення роботи бота
ДОДАТКОВО:
    - Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися невірною,
        та бот буде виводити повідомлення "Invalid command."
    - Обробка винятків за допомогою докоратора   
'''

# Декоратор для обробки помилок
def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Enter the name of contact"
    return inner

# Функція для розбору введеного користувачем рядка на команду та її аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Обгорнення декоратором функції
@input_error
# Функція для додавання нового контакта
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Обгорнення декоратором функції
@input_error
# Функція для зміни телефона існуючого контакту
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Failed, contact not fount."


# Функція для відображення номера телефона по імені контакта
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Failed, name not fount."


# Функція для показу усіх записів контактів
def show_all(contacts):
    result_string = ""
    for name, phone in contacts.items():
        result_string += f"name: {name}, phone: {phone}\n"
    return result_string


# Основний цикл обробки команд
def main():
    # Ініціалізвція словника, де будуть збережені всі контакти
    contacts = {}
    # Вітання
    print("Welcome to the assistant bot!")
    # Цикл обробки команд
    while True:
        # Отримання даних (команди та аргументи) від користувача
        user_input = input("Enter a command: ")
        # Парсинг даних на команди та аргументи
        command, *args = parse_input(user_input)
        # Команди завершення роботи бота
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Команда для привітання
        elif command == "hello":
            print("How can I help you?")
        # Команда на додавання нового контакта
        elif command == "add":
            print(add_contact(args, contacts))
        # Команда зміни телефона існуючого контакта
        elif command == "change":
            print(change_contact(args, contacts))
        # Команда для відображення номера телефона по імені контакта
        elif command == "phone":
            print(show_phone(args, contacts))
        # Команда для відображення усіх існуючих записів контактів
        elif command == "all":
            print(show_all(contacts))
        # Попередження про не правильну команду
        else:
            print("Invalid command.")


# Точка входу програми (Entry point)
if __name__ == "__main__":
    main()
