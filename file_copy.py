#copyfile()=copies contents of a file
#copy()=copyfile()+permission mode+destination can be a directory
#copy2()=copy()+copies metadata(file's creation and modification times)
import shutil
shutil.copyfile('F:\\tokee\\programming\\python\\code\\2.txt','F:\\tokee\\programming\\python\\code\\copy.txt')#src,dst