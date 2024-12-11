from datetime import datetime
temp_created_date = datetime.today()

username = input("Введите имя пользователя - ")

title = input("Заголовок\n")

content = input("Текст\n")

status = input("Статус - ")

created_date = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
issue_date = datetime.strftime(formatted_issue_date, "%d.%m")

print("\nВы ввели следующие данные:")
print("Имя пользователя", username)
print("Заголовок", title)
print("Наполнение", content)
print("Статус", status)
print("Дата создания", created_date)
print("Дата дедлайна", issue_date)