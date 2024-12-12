from datetime import datetime
temp_created_date = datetime.today()

username = input("Введите имя пользователя: ")

content = input("Введите описание заметки: \n")

status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

created_date = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
issue_date = datetime.strftime(formatted_issue_date, "%d.%m")

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)


print("\nВы ввели следующие данные:")
print("Имя пользователя", username)
print("Заголовок", titles)
print("Наполнение", content)
print("Статус", status)
print("Дата создания", created_date)
print("Дата дедлайна", issue_date)