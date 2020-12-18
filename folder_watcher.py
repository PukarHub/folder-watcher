from os import listdir
from os.path import isfile, join
from functions import give__extensions,make__Dir,move__files

mypath= "C:\\Users\\dell\\Downloads"

onlyfiles = [f for f in listdir(mypath)if isfile(join(mypath, f))]

result = onlyfiles

# Check extensions 
result = give__extensions(onlyfiles)
print(result)

# Make Directory
make__Dir(result, mypath)

# Move files to Directory
move__files(onlyfiles, mypath)












































# path = "C:\\Users\\dell\\Downloads"

# myfiles = [i for i in os.listdir(path) if os.path.isfile(path + "/" +i)]

# for ext in myfiles:
#     extsplit = ext.split(".")
#     if not os.path.isdir(path + "/" + ext[-1]):
#         os.mkdir(path + "/" + ext[-1])
#     source = path + "/" + ext
#     print(source)
#     dest = path + "/" + ext[-1]
#     shutil.move(source,dest)


