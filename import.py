import os
cwd = os.getcwd()  #current working directory
path = os.path.join("C:/PYTHON/renil", "py") #concate file path for creating folder/directory

os.makedirs(path) #makedirs used for ensure parent dirctory are created if not exist
print("current directory",cwd) 