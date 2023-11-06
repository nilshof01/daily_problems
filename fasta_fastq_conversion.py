from Bio import SeqIO
from tkinter import filedialog
from unzip_file import unzip
import os


def convert():
    file_to_change = filedialog.askopenfilename()
    print(file_to_change)
    dirname = os.path.dirname(file_to_change)
    if file_to_change.endswith(".gz"):
        unzip(file_to_change)
        file_to_change = file_to_change[:-3]
    else:
        pass
    base = os.path.basename(file_to_change).split(".")
    extension = base[1]
    filename = base[0]

    if extension in ["fasta", "fsa", "fs", "fa", "fas"]:
        handle = os.path.join(dirname, filename + ".fastq")
        with open(file_to_change, "r") as fasta, open(handle, "w") as fastq:
            for record in SeqIO.parse(fasta, "fasta"):
                record.letter_annotations["phred_quality"] = [40] * len(record)
                SeqIO.write(record, fastq, "fastq")
    elif extension in ["fastq", "fq"]:
        handle = os.path.join(dirname, filename + ".fasta")
        SeqIO.convert(file_to_change, "fastq", handle, "fasta")

if __name__ == '__main__':
    convert()
    
    