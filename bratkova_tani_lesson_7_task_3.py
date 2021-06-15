import os
import shutil


def create_file(path_new_file, file_name): # эта функция умеет создавать файл в папке, в которой ее попросят
    os.chdir(path_new_file)
    if not os.path.isfile(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            print(f'Создан файл {file_name} в папке {path_new_file}')
    else:
        print(f'уже существует файл {file_name} в папке {path_new_file}')


# Создадим папок
print(os.getcwd())

print('\nСодание папок: ')
folders_list = ['my_project',
                  'my_project\\settings',
                  'my_project\\mainapp\\templates\\mainapp',
                  'my_project\\authapp\\templates\\authapp']

for dir_new in folders_list:
    if not os.path.isdir(dir_new):
        os.makedirs(dir_new)
        print(f'создана папка {os.path.abspath(dir_new)}')
    else:
        print(f'уже существует папка {os.path.abspath(dir_new)}')

# Создадим файлы
print('\nСодание файлов: ')
current_dir = os.getcwd() # это если мы будем использовать модуль в других папках

dir_in_func = os.path.join(current_dir, r'my_project\authapp\templates\authapp')
create_file(dir_in_func, 'base.html')
create_file(dir_in_func, 'index.html')

dir_in_func = os.path.join(current_dir, r'my_project\mainapp\templates\mainapp')
create_file(dir_in_func, 'base.html')
create_file(dir_in_func, 'index.html')

dir_in_func = os.path.join(current_dir, r'my_project\settings')
create_file(dir_in_func, '__init__.py')
create_file(dir_in_func, 'dev.py')
create_file(dir_in_func, 'prod.py')

dir_in_func = os.path.join(current_dir, r'my_project\mainapp')
create_file(dir_in_func, '__init__.py')
create_file(dir_in_func, 'models.py')
create_file(dir_in_func, 'views.py')

dir_in_func = os.path.join(current_dir, r'my_project\authapp')
create_file(dir_in_func, '__init__.py')
create_file(dir_in_func, 'models.py')
create_file(dir_in_func, 'views.py')

# for root, dirs, files in os.walk(current_dir): # это был костыль
#     for file in files:
#         if file.lower().endswith('.html'):
#             print(os.path.basename(file))
#             # print(os.path.join(root,file))
#             print(os.path.dirname(file))

current_dir_1 = os.path.join(current_dir, 'my_project')

files_html = [os.path.join(root,file) for root, dirs, files in os.walk(current_dir_1) for file in files if file.lower().endswith('.html')]

print('\nПути где лежат файлы с расширением .html')
print(files_html, type(files_html))

os.chdir(os.path.join(current_dir, r'my_project'))

try:
    os.mkdir('templates')
except FileExistsError:
    print('каталог "templates" существует')

source = os.path.join(current_dir, r'my_project\authapp\templates\authapp')
destination = os.path.join(current_dir, r'my_project\templates\authapp')
if not os.path.isdir(destination):
    shutil.copytree(source, destination)

source = os.path.join(current_dir, r'my_project\mainapp\templates\mainapp')
destination = os.path.join(current_dir, r'my_project\templates\mainapp')
if not os.path.isdir(destination):
    shutil.copytree(source, destination)
