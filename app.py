import os

def rename_files(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        dst = f"{prefix}{str(count)}{os.path.splitext(filename)[1]}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, dst)
        os.rename(src, dst)
    print("Files renamed successfully.")

directory = input("Enter directory path: ")
prefix = input("Enter prefix for new filenames: ")
rename_files(directory, prefix)
