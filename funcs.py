import os
from shutil import rmtree

def create_dir(dir_name):
    try:
        static_path = os.path.join(os.getcwd(), 'static', 'img')
        path_dir = os.path.join(static_path, dir_name)
        if not os.path.isdir(path_dir):
            os.mkdir(path_dir)
        return path_dir
    except:
        return None


def delete_dir(dir_name):
    try:
        static_path = os.path.join(os.getcwd(), 'static', 'img')
        path_dir = os.path.join(static_path, dir_name)
        #os.rmdir(path_dir)
        rmtree(path_dir)
        return True
    except:
        return False

def get_dir(dir_name):
    try:
        static_path = os.path.join(os.getcwd(), 'static', 'img')
        path_dir = os.path.join(static_path, dir_name)
        if os.path.isdir(path_dir):
            return path_dir
        else:
            return False
    except:
        return None