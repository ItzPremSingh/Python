from os import walk


pattern = "dirfind"  # input("Enter pattern:")

for path, folder, files in walk("../Program/"):
    for directory in folder:
        if pattern in directory:
            print(directory)

    for file in files:
        if pattern in file:
            print(file)
