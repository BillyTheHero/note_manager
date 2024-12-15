from datetime import datetime
temp_created_date = datetime.today()

note = {}

note ["username"] = input("Введите имя пользователя: ")

note ["content"] = input("Введите описание заметки: \n")

note ["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

note ["created_date"] = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
note ["issue_date"] = datetime.strftime(formatted_issue_date, "%d.%m")

titles = []
while True:
    title  = input(f"Введите заголовок заметки или нажмите Enter: ")
    if title == "":
        break
    titles.append(title)
note ["titles"] = titles

print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
