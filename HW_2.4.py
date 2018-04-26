import os
import chardet


migration = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def decode_file(file_name):
    with open(os.path.join(current_dir, migration, file_name), 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data
    return data


def sql_files():
    sql_files_list = []
    for d, dirs, files in os.walk(current_dir):
        for filename in files:
            if filename.endswith('.sql'):
                sql_files_list.append(filename)
    return sql_files_list


def search_string(sql_files_list):
    file_list = sql_files_list
    search_history = []
    while True:
        search = input('Введите строку, которая содержится в файлах: ')
        search = search.lower()
        founds_files = []

        if search != 'go back':
            for file_name in file_list:
                if search in decode_file(file_name):
                    founds_files.append(file_name)
                    print(file_name)
            search_history.append(founds_files)
            print('Всего: {}'.format(len(founds_files)))
            file_list = founds_files

        if search == 'go back':
            del search_history[-1]
            try:
                for i in range(len(search_history[-1])):
                    print(search_history[-1][i], end='\n')
                print('Всего: {}'.format(len(search_history[-1])))

            except IndexError:
                print('К сожалению, история пустая')


if __name__ == '__main__':
    print('*' * 140)
    print('Введите часть содержимого файла, например "INSERT".')
    print('Если вы хотите посмотреть результат предыдущего поиска введите "go back".')
    print('*' * 140)
    search_string(sql_files())

    pass
