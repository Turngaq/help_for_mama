# HELP FOR MAMA v2.0
# Программа для анализа данных из Excel файла 

Данная программа предназначена для анализа данных, содержащихся в Excel файле. Программа выполняет расчет возраста на основе указанных дат рождения и анализирует пол указанных лиц.

## Установка

Для запуска программы вам потребуется установленный интерпретатор Python версии 3.x и несколько дополнительных библиотек. Вы можете установить библиотеки с помощью следующей команды:

`pip install pandas tabulate`


## Запуск программы

Для запуска программы выполните следующие шаги:

1. Перейдите в папку, где находится файл main.py.
2. Запустите командную строку или терминал
3. Запустите программу с помощью команды:

`python main.py`


Программа предложит вам выбрать Excel файл с данными, указать названия столбцов с датой рождения и полом. После анализа данных, программа выведет результат в виде красивой таблицы.

## Примечание

- Программа предполагает, что Excel файл имеет как минимум два столбца: один для даты рождения и другой для пола.
- Для удобства пользователя программа использует графический интерфейс для выбора файла Excel.
- Если в данных обнаружены пропущенные значения или недопустимые значения пола, программа предоставит информацию о проблемных строках.

## Автор

pavel.tarkhoff