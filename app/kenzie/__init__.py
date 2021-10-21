import os


def make_directory():
    if os.path.exists('./files_directory'):
        pass
    else:
        os.system(f'mkdir ./files_directory')
        os.system(f'mkdir ./files_directory/gif')
        os.system(f'mkdir ./files_directory/png')
        os.system(f'mkdir ./files_directory/jpg')
