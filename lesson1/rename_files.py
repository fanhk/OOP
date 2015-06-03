__author__ = 'fhk'
import os


def rename_files():
    # 1)get file names in a folder
    file_lists = os.listdir(r"C:\Users\fhk\Desktop\algo")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\fhk\Desktop\algo")

    # 2)for each file,rename filename
    for file_name in file_lists:
        print("Old name - " + file_name)
        new_name = file_name.translate(None, "0123456789")
        print("New name - " + new_name)
        os.rename(file_name, new_name)

    os.chdir(saved_path)
rename_files()
