"""This Program are change the name of all file with capitalize.
specific format name are change in 1,2,3,4... name.
 also some specific file are not affected. """
import os


def solider(path, file, for_mat):
    os.chdir(path)
    i = 1
    filelist = os.listdir(path)

    with open(file) as f:
        file_nochange = f.read().split("\n")

    for file in filelist:
        if file not in file_nochange:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == for_mat:
            os.rename(file, f"{i}{for_mat}")
            i += 1


if __name__ == '__main__':
    solider(r"E:\Code\Django", r"E:\Code\Python\name.txt", ".jpg")
    print("Work Done...!")
