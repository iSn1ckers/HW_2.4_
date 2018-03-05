import os
import chardet


migration = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def all_files_list():
    migration_dir = os.path.join(current_dir, migration)
    files_list = os.listdir(path=migration_dir)
    return files_list


def decode_file(file_name):
    with open(os.path.join(current_dir, migration, file_name), 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data
    return data


def sql_files(files_list):
    sql_files_list = []
    for file_name in files_list:
        if file_name.endswith('.sql'):
            sql_files_list.append(file_name)
    return sql_files_list


def search_string(sql_files):
    file_list = sql_files_list
    while True:
        search = input('Введите строку, которая содержится в файлах: ')
        search = search.lower()
        founds_files = []
        for file_name in file_list:
            if search in decode_file(file_name):
                founds_files.append(file_name)
                print(file_name)
        print('Всего: {}'.format(len(founds_files)))
        file_list = founds_files


if __name__ == '__main__':
    search_string(sql_files(all_files_list()))