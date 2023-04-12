import json
import csv
from sklearn.model_selection import train_test_split

def clean_text(text):
    return text.replace("\t", " ").replace("\n", " ")

def squad_to_tsv(squad_data, output_file):
    line_count = 0
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for article in squad_data:
            for paragraph in article['paragraphs']:
                context = clean_text(paragraph['context'])
                for qa in paragraph['qas']:
                    question = clean_text(qa['question'])
                    if len(qa['answers']) > 0:
                        answer = clean_text(qa['answers'][0]['text'])
                        if context and question and answer:
                            tsv_writer.writerow([context, question, answer])
                            line_count += 1
    return line_count

def load_squad_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        squad_data = json.load(f)['data']
    return squad_data

input_file = "merged_dataset.json"
train_output_file = "train_qg.tsv"
valid_output_file = "valid_qg.tsv"

squad_data = load_squad_data(input_file)

train_data, valid_data = train_test_split(squad_data, test_size=0.2, random_state=42)

train_line_count = squad_to_tsv(train_data, train_output_file)
valid_line_count = squad_to_tsv(valid_data, valid_output_file)

print(f"Number of lines in train file: {train_line_count}")
print(f"Number of lines in valid file: {valid_line_count}")
print(f"Total number of lines: {train_line_count + valid_line_count}")