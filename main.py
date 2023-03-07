import os, shutil

KEY_FOR_SEARCH = input('Что будем искать?\n')
PATH_FOR_COPY = input('Куда сохранять найденное?\n')


def search():
    for adress, dirs, files in os.walk(input('Введите путь для старта\n')):
        if adress == PATH_FOR_COPY:
            continue
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(adress, file)


def read_from_path_txt(path):
    with open(path) as r:
        for i in r:
            if KEY_FOR_SEARCH in i:
                return copy(path)


def copy(path):
    file_name = path.split('\\')[-1]
    count = 1
    while True:
        if os.path.isfile(os.path.join(PATH_FOR_COPY, file_name)):
            if f'({count - 1})' in file_name:
                file_name = file_name.replace(f'({count - 1})', '')
            file_name = f'({count}).'.join(file_name.split('.'))
            count += 1
        else:
            break

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, file_name))
    print('Скопирован файл ', file_name)


for i in search():
    try:
        read_from_path_txt(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY, 'errors_log.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')


