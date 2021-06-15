"""
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
"""

import os

dir_root = 'my_project'

if not os.path.isdir(dir_root):
    os.mkdir(dir_root)  # создать пустую папку в корне)
    print(f'создана папка {os.path.abspath(dir_root)}')
else:
    print(f'папка {os.path.abspath(dir_root)} уже существует')

os.chdir(dir_root) # переходим в папку 'my_project'

folders_list = ['settings', 'mainapp', 'adminapp', 'authapp']

for dir_new in folders_list:
    if not os.path.isdir(dir_new):
        os.mkdir(dir_new)
        print(f'создана папка {os.path.abspath(dir_new)}')
    else:
        print(f'папка {os.path.abspath(dir_new)} уже существует')

print()

for root, dir, files in os.walk(os.getcwd()):
     print(root, dir, files)
