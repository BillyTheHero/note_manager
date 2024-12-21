from datetime import datetime

# Объявляю функцию set_status() проверки статуса, чтобы не нагружать код
def set_status():
    while True:
        status = input("Введите статус заметки (например, 'Активна', 'Выполнена', 'Отложена'): ").lower()
        if status in statuses_zametki:
            print(f"{status} - статус вашей заметки")
            return status
        else:
            print("Вы ввели неправильный статус заметки. Попробуйте ещё раз.")

# Разгружаю код функцией вывода записанной информации в словарь
def set_result():
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")

# Функция для ввода и проверки даты дедлайна
def set_issue_date():
    while True:
        temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
        try:
            formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
            return formatted_issue_date  # Возвращаем объект datetime
        except ValueError:
            print("Неверный формат даты. Попробуйте снова.")

# Функция вывода списка
def viewing():
    print("\nВсе сохранённые заметки:")
    for note in notes:
        print(f"ID: {note['id']}, Пользователь: {note['username']}, Описание: {note['content']}")

# Объявляю переменную-флаг для использования ее в цикле
continue_input = True

# Инициализация списка
notes = []

# Создание заметки
while continue_input:
    menu = input("Здравствуйте, вас приветсвует приложение заметки\nС помощью кнопок навигации выберите пункт меню\nН - создать новую заметку\nП - посмотреть созданные\nУ - удалить заметки\n").lower()
    if menu == "н":
        while True:
            # Задаю статичные переменные
            note = {}
            statuses_zametki = ["активна", "выполнена", "отложена"]

            # Заполняю словарь
            note["username"] = input("Введите имя пользователя: ")
            note["content"] = input("Введите описание заметки: ")
            note["status"] = set_status()
            note["id"] = len(notes) + 1

            # Программа получает сегодняшнюю дату
            temp_created_date = datetime.today()
            note["created_date"] = temp_created_date  # Сохраняем объект datetime

            # Ввод и проверка даты дедлайна
            note["issue_date"] = set_issue_date()

            # Проверка даты создания и даты дедлайна с выводом разницы
            while True:
                difference_date = note["issue_date"] - note["created_date"]
                if difference_date.days >= 0:
                    print(f"Разница в днях: {difference_date.days} дней")
                    note["difference_date"] = difference_date.days  # Сохраняем разницу в днях
                    break
                else:
                    print("Дата дедлайна не может быть раньше даты создания заметки.")
                    note["issue_date"] = set_issue_date()  # Запрашиваем дату заново

            # Ввод заметок столько, сколько хочет пользователь
            titles = []
            print("Введите заголовки заметок (нажмите Enter, чтобы завершить):")
            while True:
                title = input("Заголовок: ")
                if not title:
                    break
                titles.append(title)
            note["titles"] = titles

            # Вывод информации
            set_result()

            # Программа задает вопрос пользователю о смене статуса заметки
            change_zametki = input("\nЖелаете ли изменить статус заметки? д/н: ").lower()
            while True:
                if change_zametki == "д":
                    note["status"] = set_status()
                    break
                elif change_zametki == "н":
                    print("Статус заметки не изменен.")
                    break
                else:
                    change_zametki = input("Вы указали не верный ответ, выберите д/н\nЖелаете ли изменить статус заметки? д/н: ").lower()

            # Обновленная информация заметки
            print("\nОбновлённая информация о заметке:\n")
            set_result()

            # Сохранение заметки в список
            while True:
                save_notes = input("Желаете ли вы сохранить свою заметку? д/н: ").lower()
                if save_notes == "н":
                    print("Заметка не сохранена")
                    break
                elif save_notes == "д":
                    notes.append(note)
                    print("Заметка сохранена")
                    print(f"Заметка сохранена с ID: {note['id']}")
                    break
                else:
                    save_notes = input("Выберите д/н\nЖелаете ли вы сохранить свою заметку? д/н: ").lower()
                    break

            # Создание новой заметки
            while True:
                new_notes = input("Желаете ли создать еще заметку? д/н: ").lower()
                if new_notes == "н":
                    continue_input = False
                    break
                elif new_notes == "д":
                    print("Создание новой заметки")
                    break
                else:
                    new_notes = input("Выберите д/н\nЖелаете ли создать еще заметку? д/н: ").lower()
            if not continue_input:
                break

        # Просмотр списка после добавления
        while True:
            viewing_after_addet = input("Желаете ли посмотреть свои заметки? д/н: ")
            if viewing_after_addet == "н":
                break
            elif viewing_after_addet == "д":
                viewing()
                break
            else:
                print("Выберите д/н")
                viewing_after_addet = input("Желаете ли посмотреть свои заметки? д/н")
                break

    # Просмотр заметок
    elif menu == "п":
        viewing()