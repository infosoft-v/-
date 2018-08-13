from os import path, makedirs, walk
from shutil import make_archive, rmtree
import subprocess
import json
import os

# project_name:str
# path_root: str
folder_src = r"SRC"
# path_src = ""
# folder_app: str
# path_app = ""
# folder_arc: str
# path_arc:str


def clear_source_folder(path: str = folder_src):
    for root, dirs, files in walk(path):
        for dir in dirs:
            # print("удаление каталога: {}".format(path.join(root, dir)))
            rmtree(path.join(root, dir), True)
    print("Очищен каталог {}".format(path))


def get_path_oper(file: str, oper_mode: str):
    path:str = ""
    if oper_mode == "dec":
        pass
    elif oper_mode == "enc":
        pass

    return path


def module_decode(file: str):
    path_oper = get_path_oper("dec", file)
    _gcomp = "gcomp.exe"
    file_name = file

    command_line = "cmd /C " + _gcomp + " -d -F " + file_name + " -D " + path_oper
    print(command_line)
    # ЗапуститьПриложение(Команда, КаталогПроекта, Истина)
    proc = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE)


def project_decode():
    path_src = path.join(path_root, folder_src)
    if not path.exists(path_src):
        makedirs(path_src)
    else:
        clear_source_folder(path_src)

    for root, dirs, files in walk(path.join(path_root, folder_app)):
        for file in files:
            if file.endswith(".ert"):
                print("разбор модуля {}".format( path.join(root, file)))
                module_decode(file)
    print("Разборка проекта завершена")


def Project_Archive():
    file_name:str = ""
    archive_name = project_name + file_name + ".zip"
    archive_path = path.join(path.join(path_root, folder_arc, archive_name))
    make_archive(archive_path, 'zip', path_app)


def Write_JSON():

    dir = {
        "Path_Root" : r"E:\Work\SRC",
        "Folder_Src" : r"SRC",
        "Folder_App" : r"App",
        "Folder_Arc" : r"Arc",
    }
    project_name = "contur"
    data = {}
    data.setdefault(project_name, dir)
    with open(os.path.join(path_root, "config.json"), "w") as f:
          json.dump(data, f, indent=4, sort_keys=False )


def read_config():
    pass


source_Exts: list = ["bsl", "os"]
path_root = r"E:\Work"
folder_src = r"SRC"
path_src = path.join(path_root, folder_src)
folder_app = r"App"
path_app = path.join(path_root, folder_app)
folder_arc = r"Arc"
path_arc = path.join(path_root, folder_arc)

Write_JSON()

read_config()
task_mode = "dec"

if task_mode == "dec":
    project_decode()


elif task_mode == "enc":
    pass

else:
    print("Не определен режим задачи!")
