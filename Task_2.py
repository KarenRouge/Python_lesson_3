def user_info(name, family_name, year_birth, permanent_residence, Email, phone_number):
    return (name, family_name, year_birth, permanent_residence, Email, phone_number)

name = str(input("Введите свое имя: "))
family_name = str(input("Введите свою фамилию: "))
year_birth = str(input("Введите дату Вашего рождения: "))
permanent_residence = str(input("Введите город Вашего проживания: "))
Email = str(input("Введите адрес Вашей электронной почты: "))
phone_number = str(input("Введите Ваш номер телефона: "))

print(user_info(name, family_name, year_birth, permanent_residence, Email, phone_number))
