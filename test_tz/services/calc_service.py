from datetime import datetime, date
import csv
import allure


@allure.step("Вычисление числа Фибоначчи")
def get_fibonachi_num(n: int) ->int:
    f1, f2 = 0, 1
    for i in range(n):
        # print(f1)
        f1, f2 = f2, f1 + f2
    return f1


@allure.step("Вычисление числа Фибоначчи по текущему дню месяца")
def get_fibonachi_of_current_day():
    """
    Функуция вычисляет N-е число Фибоначчи, где N - это текущий день месяца + 1
    :return: N-е число Фибоначчи
    """
    day_number = date.today().day + 1
    return get_fibonachi_num(day_number)


@allure.step("Проверка правильности заполнения таблицы")
def check_table_content(table_content, deposit_sum):
    result = ""
    if len(table_content) != 2:
        result += "Amount of transaction must be 2.\n"
    for index, row in enumerate(table_content):
        if deposit_sum != int(row[1]):
            result += f"Amount in row {index} is not equivalent to {deposit_sum}\n"

    if table_content[0][2] !="Credit":
        result += f"Transaction Type in row 0 must be 'Credit'"
    if table_content[1][2] !="Debit":
        result += f"Transaction Type in row 1 must be 'Debit'"
    return result


@allure.step("Переформатирование даты")
def convert_date_to_format_from_tz(date: str):
    date_input = datetime.strptime(date, '%b %d, %Y %I:%M:%S %p')
    date_converted = date_input.strftime('%d %B %Y %H:%M:%S')
    return date_converted


@allure.step("Сохранение данных из таблицы в файл *.csv")
def save_transaction_to_csv_file(table_content, filename: str):
    with open(filename, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=" ", lineterminator="\n")
        for row in table_content:
            converted_date = convert_date_to_format_from_tz(row[0])
            row[0] = converted_date
            file_writer.writerow(row)

    allure.attach.file(source=filename, name=filename, attachment_type=allure.attachment_type.CSV)
