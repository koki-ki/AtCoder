import glob
import os


print(glob.glob('./test/*'))
dirnames = os.listdir('.')
print(dirnames)

for dir in dirnames:
    files = glob.glob(dir + '/*')
    for f in files:
        new_file_name = f.replace('/', '_')
        print(new_file_name)
        os.rename(f, new_file_name)