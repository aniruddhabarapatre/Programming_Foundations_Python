import os
from os import listdir

def rename_files():
    file_list = listdir("/Users/aniruddhabarapatre1/Learn/Udacity/Programming_Foundations_with_Python/prank")
    print(file_list)

    current_path = os.getcwd()
    os.chdir("/Users/aniruddhabarapatre1/Learn/Udacity/Programming_Foundations_with_Python/prank")

    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(current_path)
    
rename_files()    

    
