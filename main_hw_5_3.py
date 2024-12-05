# Домашнє завдання: Модуль - 5, завдання - 3 (не обов'язкове). Python Core 2.0. (PYTHON SOFTWARE ENGINEERING. Гнучкий формат)
'''
ОПИС:
    Скрипт для аналізу лог-файлів. Скрипт читає лог-файл, переданий
    як аргумент командного рядка, та виводить статистику за рівнями логування наприклад,
    INFO, ERROR, DEBUG, WARNING. Також користувач може вказати рівень логування як другий
    аргумент командного рядка, щоб отримати всі записи цього рівня.
ВХІДНІ АРГУМЕНТИ:
    - шлях до лог-файлу
    - рівень логування, один із <INFO, ERROR, DEBUG, WARNING>
ПРИКЛАД ВИКОРИСТАННЯ:
    в командному рядку потрібно ввести:
    python main_hw_5_3.py ./logfile.log info
'''

# Імпорт необхідних модулів
from pathlib import Path
from sys import argv
# Парсинг аргументів та їх аналіз
if len(argv) > 2:
    path = Path(argv[1])
    log_level = str(Path(argv[2]))
elif len(argv) > 1:
    path = Path(argv[1])
    log_level = "without"
# Обробка помилок аргументів
else:
    print("Помилка, введіть шлях до лог-файлу як аргумент в командному рядку")
    exit()
if log_level.lower() not in ["info", "debug", "error", "warning", "without"]:
    print("Помилка, введіть коректний аргумент рівня логування")
    exit()
if path.suffix.lower() != ".log":
    print(f"Помилка, файл {path} має не привильне розширення")
    exit()


# Парсинг рядків лог-файлу
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}

# Завантаження логів з файлу
def load_logs(file_path: str) -> list:
    global list_of_dict
    list_of_dict = []
    with open(file=file_path, mode="r", encoding="utf-8") as fh:
        while True:
            line = fh.readline().strip()
            if not line:
                break
            list_of_dict.append(parse_log_line(line))
        return list_of_dict


# Фільтрація логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level]


# Підрахунок записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    info = len([log for log in logs if log["level"].lower() == "info"])
    debug = len([log for log in logs if log["level"].lower() == "debug"])
    error = len([log for log in logs if log["level"].lower() == "error"])
    warning = len([log for log in logs if log["level"].lower() == "warning"])
    return {"INFO": info, "DEBUG": debug, "ERROR": error, "WARNING": warning}


# Форматування та вивід результатів
def display_log_counts(counts: dict):
    print()
    print(f"{"Рівень логування":<17}| {"Кількість":<}")
    print("-"*17+"|"+"-"*10)
    for key, value in counts.items():
        print(f"{key:<17}| {value:<}")
    if log_level == "without":
        exit()
    else:
        print()
        print(f"Деталі логів для рівня '{log_level.upper()}':")
        for item in filter_logs_by_level(list_of_dict, log_level):
            print(f"{item["date"]} {item["time"]} - {item["message"]}")


# Обробка винятків роботи з файлом
try:
    display_log_counts(count_logs_by_level(load_logs(path)))
except FileNotFoundError:
    print(f"Помилка, файл '{path}' не знайдено")
except IndexError:
    print(f"Помилка, файл '{path}' має не правильну структуру")