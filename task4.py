# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(data):
    count = 1
    res = ''
    ress = []
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            ress.append(str(count) + data[i])
            res = res + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        ress.append(str(count)+ data[-1])
        res = res + str(count) + data[-1]
    return [res,ress]


def restore(data):
    res = ''
    for i in range(len(data)):
            print("str = lst[i] =" + data[i])
            str = data[i]
            char = str[-1]
            number = str[:-1]
            res = res + char*int(number)
    return res

s = input("Введите текст для сжатия: ")
print(f"Текст после сжатия: {compression(s)[0]}")
print(f'Текст после восстановления: {restore(compression(s)[1])}')

