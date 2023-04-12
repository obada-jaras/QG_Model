import csv

def read_tsv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        lines = 0
        for row in tsv_reader:
            lines += 1
    return lines

train_lines = read_tsv_file("D:/New folder/Model/train_qg.tsv")
valid_lines = read_tsv_file("D:/New folder/Model/valid_qg.tsv")

print(f"Number of lines in train file: {train_lines}")
print(f"Number of lines in valid file: {valid_lines}")
