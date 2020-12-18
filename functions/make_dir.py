import os
from os.path import isfile, join
def make__Dir(extensions, mypath):
    for folder in extensions:
        try:
            os.mkdir(os.path.join(mypath, folder))
        except FileExistsError as error:
            print(folder, 'exists')