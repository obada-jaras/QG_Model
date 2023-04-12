import csv

def create_small_dataset(input_file, output_file, num_samples):
    with open(input_file, 'r', encoding='utf-8', newline='') as f_in, open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        tsv_reader = csv.reader(f_in, delimiter='\t', quotechar='"')
        tsv_writer = csv.writer(f_out, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for idx, row in enumerate(tsv_reader):
            if idx < num_samples:
                tsv_writer.writerow(row)
            else:
                break

train_input_file = "train_qg.tsv"
valid_input_file = "valid_qg.tsv"

train_output_file = "small_train_qg.tsv"
valid_output_file = "small_valid_qg.tsv"

create_small_dataset(train_input_file, train_output_file, 500)
create_small_dataset(valid_input_file, valid_output_file, 100)

print("Small dataset files created.")
