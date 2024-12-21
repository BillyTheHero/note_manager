from datetime import datetime


# Функция проверки статуса
statuses_zametki = ["активна", "выполнена", "отложена"]

def set_status():
    while True:
        status = input("Введите статус заметки (например, 'Активна', 'Выполнена', 'Отложена'): ").lower()
        if status in statuses_zametki:
            print(f"{status} - статус вашей заметки")
            return status
        else:
            print("Вы ввели неправильный статус заметки. Попробуйте ещё раз.")


# Функция вывода записанной информации в словарь
def set_result(note):
    for key, value in note.items():
        if key == "difference_date":
            print(f"Разница в днях: {value} дней")
        elif isinstance(value, datetime):
            print(f"{key.capitalize()}: {value.strftime('%d.%m.%Y')}")
        else:
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
notes = []

def viewing():
    if not notes:
        print("\nСписок заметок пуст.")
        return

    print("\nВсе сохранённые заметки:")
    for note in notes:
        print(f"ID: {note['id']}, Пользователь: {note['username']}, Описание: {note['content']}")


def created_note():
    note = {}
    note["username"] = input("Введите имя пользователя: ")
    note["content"] = input("Введите описание заметки: ")
    note["status"] = set_status()
    note["id"] = len(notes) + 1

    # Программа получает сегодняшнюю дату
    # Сверяет ее с датой deadline
    while True:
        temp_created_date = datetime.today()
        note["created_date"] = temp_created_date
        note["issue_date"] = set_issue_date()
        while True:
            difference_date = note["issue_date"] - note["created_date"]
            if difference_date.days >= 0:
                print(f"Разница в днях: {difference_date.days} дней")
                note["difference_date"] = difference_date.days
                break
            else:
                print("Дата дедлайна не может быть раньше даты создания заметки.")
                note["issue_date"] = set_issue_date()

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
        set_result(note)

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
                change_zametki = input(
                    "Вы указали не верный ответ, выберите д/н\nЖелаете ли изменить статус заметки? д/н: ").lower()

        # Обновленная информация заметки
        print("\nОбновлённая информация о заметке:\n")
        set_result(note)

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
                break
            elif new_notes == "д":
                print("Создание новой заметки")
                return created_note()
            else:
                new_notes = input("Выберите д/н\nЖелаете ли создать еще заметку? д/н: ").lower()
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


# Удаление заметки
def delete_note():
    try:
        viewing()
        note_id = int(input("Введите id заметки для ее удаления: "))
        note_to_delete = next(note for note in notes if note["id"] == note_id)
        notes.remove(note_to_delete)
        print(f"Заметка с ID {note_id} удалена.")

    except StopIteration:
        print(f"Заметка с ID {note_id} не найдена.")
    except ValueError:
        print("Вы ввели некорректный ID. Введите число.")


# Создание заметки
def main_menu():
    while True:
        menu = input(
            "\nЗдравствуйте, вас приветствует приложение Заметки\n"
            "Выберите пункт меню:\n"
            "Н - создать новую заметку\n"
            "П - посмотреть созданные заметки\n"
            "У - удалить заметки\n"
            "В - выйти\n"
        ).lower()

        if menu == "н":
            created_note()
        elif menu == "п":
            viewing()
        elif menu == "у":
            delete_note()
        elif menu == "в":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main_menu()