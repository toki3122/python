import os
import shutil
path='test.txt'
try:
    os.remove(path)#deletes a file
    os.rmdir(path)#deletes an empty folder
    shutil.rmtree(path)#deletes an folder containing files
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+" was deleted")