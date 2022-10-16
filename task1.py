# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data = input("Введите текст:\n")

word_find = "абв"

lst = [i for i in data.split() if word_find not in i]

print(f'Полученный текст: {" ".join(lst)}')