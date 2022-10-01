import glob
import os
import shutil

cdir = os.getcwd()
files = os.listdir(cdir)
files_file = [f for f in files if os.path.isfile(os.path.join(cdir, f))]

for f in files_file:
    print('Now:', f)
    if f == 'move2.py' or f == '133':
        continue
    folder_name, file_name = f.split('_', 1)
    print(folder_name, file_name)
    if not os.path.exists(os.path.join(cdir, folder_name)):
        os.mkdir(os.path.join(cdir, folder_name))
    new_path = shutil.move(os.path.join(
        cdir, f), os.path.join(cdir, folder_name, file_name))
