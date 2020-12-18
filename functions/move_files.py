import os
import shutil
def move__files(onlyfiles, mypath):
    for i in onlyfiles:
        source = os.path.join(mypath, i)
        extsplit = i.split(".")[-1]
        print(source)
        destination = os.path.join(mypath, extsplit)
        print(destination)
        try:
            shutil.move(source, destination)
        except FileExistsError as error:
            print(folder, 'exists')