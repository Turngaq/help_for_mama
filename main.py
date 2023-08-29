from datetime import datetime
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calculate_age(birthdate, reference_date):
    age = reference_date.year - birthdate.year - (
                (reference_date.month, reference_date.day) < (birthdate.month, birthdate.day))
    if (birthdate.month, birthdate.day) == (2, 29) and not is_leap_year(reference_date.year):
        age -= 1
    return age


def main():
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно tkitnter

    file_path = filedialog.askopenfilename(title="Выберете файл Exel", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        print("Файл не выбран")
        return

    date_column = input("Введите название столбца с датой рождения: ")
    gender_column = input("Введите название столбца с полом: ")

    data = pd.read_excel(file_path)
    current_date = datetime.now()

    data[date_column] = pd.to_datetime(data[date_column])
    data['Возраст'] = data[date_column].apply(lambda x: calculate_age(x, current_date))  # Возраст в годах

    data[gender_column] = data[gender_column].apply(lambda x: "Мальчики" if x == "м" else ("Девочки" if x == "д" else x))

    # Проверка на пропущенные значения
    missing_values = data[data[date_column].isnull() | data[gender_column].isnull()]
    if not missing_values.empty:
        print("Обнаружены строки с пропущенными данными:")
        print(missing_values)
        return

    # Проверка на недопустимые значения в столбце пола
    invalid_gender_values = data[~data[gender_column].isin(['Мальчики', 'Девочки'])]
    if not invalid_gender_values.empty:
        print("Обнаружены недопустимые значения в столбце пола:")
        print(invalid_gender_values)
        return

    result = data.groupby(['Возраст', gender_column]).size().unstack(fill_value=0)
    print(tabulate(result, headers='keys', tablefmt='pretty'))


if __name__ == "__main__":
    main()
