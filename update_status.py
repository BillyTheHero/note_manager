from datetime import datetime

#Объявляю функцию set_status() проверки статуса, чтобы не нагружать код
def set_status():
    while True:
        status = input("Введите статус заметки (например, 'Активна', 'Выполнена', 'Отложена'): ").lower()
        if status in statuses_zametki:
            print(f"{status} - статус вашей заметки")
            return status
        else:
            print("Вы ввели неправильный статус заметки. Попробуйте ещё раз.")

#Разгружаю код функцией вывода записанной информации в словарь
def set_result():
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")

#Задаю статичные переменные
note = {}
statuses_zametki = ["активна", "выполнена", "отложена"]

#Заполняю словарь
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: \n")
note["status"] = set_status()
#
temp_created_date = datetime.today()
note["created_date"] = temp_created_date.strftime("%d.%m")

#Проверка формата даты
while True:
    temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
    try:
        formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
        note["issue_date"] = formatted_issue_date.strftime("%d.%m")
        break
    except ValueError:
        print("Неверный формат даты. Попробуйте снова.")

#Ввод заметок столько, сколько хочет пользователь
titles = []
print("Введите заголовки заметок (нажмите Enter, чтобы завершить):")
while True:
    title = input("Заголовок: ")
    if not title:
        break
    titles.append(title)
note["titles"] = titles

#Вывод информации
print("\nСобранная информация о заметке:\n")
print(set_result())

#Программа задает вопрос пользователю о смене статуса заметки
change_zametki = input("\nЖелаете ли изменить статус заметки? д/н: ").lower()
while True:
    if change_zametki == "д":
        note["status"] = set_status()
        break
    elif change_zametki == "н":
        print("Статус заметки не изменен.")
        break
    else:
        print("Вы указали не верный ответ, выберите д/н")
        change_zametki = input("\nЖелаете ли изменить статус заметки? д/н: ").lower()

#Обновленная информация заметки
print("\nОбновлённая информация о заметке:\n")
print(set_result())
