from pathlib import Path


# печать справочника:
def print_list():
    with open("telephone_list.txt", "r") as data_file:
        print(data_file.read())


# поиск:
def search_in_list(list_file):
    search_data = input(
        "Введите фамилию или имя (латиницей), или номер (начиная с +7) для поиска: "
    )
    found = 0
    with open("telephone_list.txt", "r") as data_file:
        for line in data_file:
            if search_data in line:
                found += 1
                print(line, end="")
    if found == 0:
        print("Не найдено")


# ввод и запись новой строки:
def write_and_add_data():
    with open("telephone_list.txt", "r") as data:
        tel_file = data.read()
        num = len(tel_file.split("\n"))
    with open("telephone_list.txt", "a") as data_file:
        first_name = input("Введите фамилию(латиницей) для добавления: ")
        second_name = input("Введите имя (латиницей) для добавления: ")
        number = input("Введите номер телеофна (начиная с +7) для добавления: ")
        data_file.write(f"{num}: {first_name}, {second_name}, {number}\n")
        print(f"Добавлено: {num}: {first_name}, {second_name}, {number}\n")


# Изменяет в справочнике:
def edit_data():
    with open("telephone_list.txt", "r") as data:
        tel_book = data.read()
        print(tel_book)
    index_edited_line = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    line_for_edit = tel_book_lines[index_edited_line]
    elements = line_for_edit.split(" ")
    first_name = input("Введите фамилию(латиницей) для добавления: ")
    second_name = input("Введите имя (латиницей) для добавления: ")
    number = input("Введите номер телеофна (начиная с +7) для добавления: ")
    num = elements[0]
    if len(first_name) == 0:
        fio = elements[1]
    if len(second_name) == 0:
        phone = elements[2]
    if len(number) == 0:
        phone = elements[3]
    edited_line = f"{num} {first_name}, {second_name}, {number}"
    tel_book_lines[index_edited_line] = edited_line
    print(f"{line_for_edit}, изменено на: {edited_line}\n")
    with open("telephone_list.txt", "w") as f:
        f.write("\n".join(tel_book_lines))


# Удаление строки:
def delete_data():
    with open("telephone_list.txt", "r") as data:
        tel_book = data.read()
        print(tel_book)
        index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
        tel_book_lines = tel_book.split("\n")
        line_to_delete = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f"Удалена запись: {line_to_delete}\n")
    with open("telephone_list.txt", "w") as data:
        data.write("\n".join(tel_book_lines))


# -------------------------------------------------------------------------------------------
