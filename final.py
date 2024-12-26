from datetime import datetime
from colorama import Fore, Back, Style

# Функция проверки статуса
statuses_zametki = ["активна", "выполнена", "отложена"]

def set_status():
    while True:
        status = input(Fore.RED + "Введите статус заметки (например, 'Активна', 'Выполнена', 'Отложена'): ").lower()
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
        temp_issue_date = input(Fore.RED + "Дата дэдлайна в формате дд.мм.гггг - ")
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
        print(f"ID: {note['id']}, Пользователь: {note['username']}, Описание: {note['content']}, Статус:{note['status']}")


def created_note():
    note = {}
    note["username"] = input(Fore.RED + "Введите имя пользователя: ")
    note["content"] = input(Fore.RED + "Введите описание заметки: ")

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
            title = input(Fore.RED + "Заголовок: ")
            if not title:
                break
            titles.append(title)
        note["titles"] = titles

        # Вывод информации
        set_result(note)

        # Программа задает вопрос пользователю о смене статуса заметки
        change_zametki = input(Fore.YELLOW + "\nЖелаете ли изменить статус заметки? д/н: ").lower()
        while True:
            if change_zametki == "д":
                note["status"] = set_status()
                break
            elif change_zametki == "н" or "":
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
            save_notes = input(Fore.YELLOW + "Желаете ли вы сохранить свою заметку? д/н: ").lower()
            if save_notes == "н":
                print("Заметка не сохранена")
                break
            elif save_notes == "д" or "":
                notes.append(note)
                print("Заметка сохранена")
                print(f"Заметка сохранена с ID: {note['id']}")
                break
            else:
                save_notes = input("Выберите д/н\nЖелаете ли вы сохранить свою заметку? д/н: ").lower()
                break

        # Создание новой заметки
        while True:
            new_notes = input(Fore.YELLOW + "Желаете ли создать еще заметку? д/н: ").lower()
            if new_notes == "н":
                break
            elif new_notes == "д" or "":
                print("Создание новой заметки")
                return created_note()
            else:
                new_notes = input("Выберите д/н\nЖелаете ли создать еще заметку? д/н: ").lower()
        break

    # Просмотр списка после добавления
    while True:
        viewing_after_addet = input(Fore.YELLOW + "Желаете ли посмотреть свои заметки? д/н: ")
        if viewing_after_addet == "н":
            break
        elif viewing_after_addet == "д" or "":
            viewing()
            break
        else:
            print("Выберите д/н")
            viewing_after_addet = input(Fore.YELLOW + "Желаете ли посмотреть свои заметки? д/н")
            break


# Удаление заметки
def delete_note():
    try:
        viewing()

        note_keyword = input("Введите ключевое слово заметки для ее удаления: ").lower()
        note_to_delete = next(note for note in notes if note["username"] or note["content"] == note_keyword)
        while True:
            confirmation = input(Fore.YELLOW + "Вы действительно хотите удалить заметку?\n")
            if confirmation == "д":
                notes.remove(note_to_delete)
                print(f"Заметка c {note_keyword} удалена.")
            elif confirmation == "н":
                print("Удаление отменено")
            else:
                print("Выберите д или н")
                break

    except StopIteration:
        print(f"Заметка не найдена.")
    except ValueError:
        print("Вы ввели некорректный ID. Введите число.")


# Поиск заметки
def search_notes():
    if not notes:
        print("Список заметок пуст. Добавьте заметки для поиска.")
        return
    keywords = input(Fore.RED + "Введите ключевые слова для поиска (через запятую): ").lower().split(',')
    results = []
    for note in notes:
        if any(keyword in note['content'].lower() for keyword in keywords):
            results.append(note)
        elif any(keyword in note['username'].lower() for keyword in keywords):
            results.append(note)
    if results:
        print(f"\nНайдено {len(results)} заметок по указанным ключевым словам:")
        for result in results:
            print(f"ID: {result['id']}, Пользователь: {result['username']}, Описание: {result['content']}")
    else:
        print("По указанным ключевым словам ничего не найдено.")


# Поиск заметки
def update_note():
    if not notes:
        print("Список заметок пуст. Сначала добавьте заметки.")
        return

    viewing()

    try:
        note_id = int(input(Fore.RED + "Введите ID заметки для обновления: "))
        note_to_update = next(note for note in notes if note["id"] == note_id)
    except StopIteration:
        print(f"Заметка с ID {note_id} не найдена.")
        return
    except ValueError:
        print("Вы ввели некорректный ID. Введите число.")
        return

    print("\nТекущая информация о выбранной заметке:")
    for key, value in note_to_update.items():
        print(f"{key.capitalize()}: {value}")

    print("\nВыберите новый статус заметки.")
    new_status = set_status()
    note_to_update["status"] = new_status

    print("\nОбновлённая информация о заметке:")
    for key, value in note_to_update.items():
        print(f"{key.capitalize()}: {value}")


# Создание заметки
def main_menu():
    while True:
        menu = input(Back.GREEN +
            "Здравствуйте, вас приветствует приложение Заметки\n"
            "Выберите пункт меню:\n"
            "Н - создать новую заметку\n"
            "П - посмотреть созданные заметки\n"
            "и - искать заметкуn\n"
            "о - обновление статуса\n"
            "У - удалить заметки\n"
            "В - выйти\n"
        ).lower()

        if menu == "н":
            created_note()
        elif menu == "п":
            viewing()
        elif menu == "и":
            search_notes()
        elif menu == "о":
            update_note()
        elif menu == "у":
            delete_note()
        elif menu == "в":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main_menu()