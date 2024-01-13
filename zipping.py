import os
import sys
import pathlib
import zipfile

dirname = input("Enter directory name that u want to backup:")
if not os.path.isdir(dirname):
    print("Directory", dirname, "doesnot exists")
    sys.exit(0)
curdirectory = pathlib.Path(dirname)
with zipfile.ZipFile("success.zip", mode="w") as archive:
    for filepath in curdirectory.rglob("*"):
        archive.write(filepath, arcname=filepath.relative_to(curdirectory))
if os.path.isfile("success.zip"):
    print("archive success created successfully")
else:
    print("Error in creating zip archive")
