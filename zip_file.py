import gzip
from tkinter import filedialog
import os



def zip_file(input_file_path):
    output_gz_path = input_file_path + ".gz"
    with open(input_file_path, 'rb') as f_in:
        with gzip.open(output_gz_path, 'wb') as f_out:
            f_out.writelines(f_in)




if __name__ == '__main__':
    while True:
        user = input("Press 1 if you want to unzip only one file in a directory, press 2 if you want to unzip multiple files")
        if user in ["1", "2"]:
            break
        else:
            print("please enter a correct value")
    if user == "1":	
        chosen_file = filedialog.askopenfilename()
        zip_file(chosen_file)
    elif user == "2":
        chosen_files = filedialog.askdirectory()
        for file in os.listdir(chosen_files):
            zip_file(os.path.join(chosen_files, file))
    else:
        pass