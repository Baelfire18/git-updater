__author__ = 'Jose Antonio Castro'
__github__ = 'Baelfire18'

import os

with open("paths.txt", 'r', encoding='utf-8') as file:
    path_list = [i.strip() for i in file.readlines()]

os.chdir('..')
main = os.getcwd()

for path in path_list:
    try:
        print(f"Running git pull for {path}")
        os.chdir(path)
        os.system("git pull")
    except Exception as error:
        print(f"Error with {path}.\n{error}\nprint('F')")
    finally:
        os.chdir(main)
        print("\n")
