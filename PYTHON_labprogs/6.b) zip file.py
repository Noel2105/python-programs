import os.path
import sys
import pathlib
import zipfile

dirc=input("Enter a folder to zip : \n")
if not os.path.isdir(dirc):
    print("Directory doesn't exists\n")
    sys.exit()
curdirc=pathlib.Path(dirc)
print(curdirc)
with zipfile.ZipFile("zipp.Zip",mode='w') as archive:
    for filepath in curdirc.rglob('*'):
        print(filepath)
        archive.write(filepath,arcname=filepath.relative_to(curdirc))
if os.path.isfile("zipp.Zip"):
    print("Archive 'zipp.Zip' created successfully")
else:
    print("Error in creating zip file")