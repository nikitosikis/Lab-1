import csv
from random import randint

with open('books.csv') as file:
    data = list(csv.DictReader(file, delimiter=';', quotechar='"'))


def task_1(data):
    return len(data)
#print(task_1(data))


def task_2(data):
    def len_n(x):
        if len(x) > 30:
            return 1
        else:
            return 0
    return sum(len_n(x['Название']) for x in data)
#print(task_2(data))


def task_3(data, author):
    for i in data:
        if author in i['Автор'] or author in i['Автор (ФИО)']:
            for j in i.keys():
                print("{:50}".format(i[j]), end='')
#task_3(data,' Маша Трауб')


def task_4(data):
    indexes = []
    while len(indexes) < 20:
        a = randint(0, len(data))
        if a not in indexes:
            if data[a]['Автор (ФИО)']:
                indexes.append(a)
    with open('data_notes.txt', 'w', encoding = 'UTF-8') as file:
        for i in indexes:
            s = data[i]['Название']
            fio = data[i]['Автор (ФИО)']
            year = int(data[i]['Дата поступления'].split(' ')[0].split('.')[2])
            print(f'{fio}. {s} - {year}', file=file)
#task_4(data)


def side_task_1(data):
        lst = []
        for item in data:
            for genre in item['Жанр книги'].split('# '):
                lst.append(genre)
        return set(lst)
#print(side_task_1(data))


def side_task_2(data):
    data_sorted = sorted(data, key=lambda x: int(x['Кол-во выдач']), reverse=True)
    for item in data_sorted[:20]:
        print(item['Название'])
#side_task_2(data)