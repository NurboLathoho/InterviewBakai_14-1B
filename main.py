# Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.1

# def zero():
#     for i in range(1, 6):
#         print(f"{i}: {'0' * 5}")
# zero()


# Напишите функцию, которая принимает список, из списка выдает случайное значение из списка и записывает результат в txt файл. Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

# import random

# def a(language_list, file_path):
#     random_language = random.choice(language_list)
#     with open(file_path, "w") as file:
#         file.write(random_language)

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]
# file_path = "random_language.txt"
# a(language, file_path)
    
# names = [“azat”, “zina”, “kuma”, “anna”, “sas”] Вывести с помощью lambda функции имена палиндромы 1

names = ["azat", "zina", "kuma", "anna", "sas"]
палиндромы = filter(lambda name: name == name[::-1], names)
print(list(палиндромы))

