import zipfile
from tkinter import filedialog
import os
import shutil
import gzip

def unzip(chosen_file):
    dir_of_file = os.path.dirname(chosen_file)
    basename = os.path.basename(chosen_file).split(".")[0]
    rest = os.path.basename(chosen_file).split(".")[1:]
    all_no_end = os.path.basename(chosen_file).split(".")[:-1]
    shutil.copy(chosen_file, os.path.join(dir_of_file, basename + "copy" + ".".join(rest)))
    if chosen_file.endswith(".gz"):
        with gzip.open(chosen_file, 'rb') as gz_file:
            file_content = gz_file.read()
            with open(os.path.join(dir_of_file, ".".join(all_no_end)), "wb") as output_file:
                output_file.write(file_content)
    elif chosen_file.endswith("zip"):
        with zipfile.ZipFile(chosen_file, 'r') as zip_ref:
            zip_ref.extractall(dir_of_file)
    else:
        return
    os.remove(os.path.join(dir_of_file, basename + "copy"+ ".".join(rest)))

if __name__ == '__main__':
    while True:
        user = input("Press 1 if you want to unzip only one file in a directory, press 2 if you want to unzip multiple files")
        if user in ["1", "2"]:
            break
        else:
            print("please enter a correct value")
    if user == "1":	
        chosen_file = filedialog.askopenfilename()
        unzip(chosen_file)
    elif user == "2":
        chosen_files = filedialog.askdirectory()
        for file in os.listdir(chosen_files):
            unzip(os.path.join(chosen_files, file))
    else:
        pass