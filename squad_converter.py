import argparse
import json

def read_squad_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_simplified_file(output_file, simplified_data):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(simplified_data, f, indent=2)

def convert_squad_to_simplified(input_file, output_file):
    squad_data = read_squad_file(input_file)
    simplified_data = []

    for article in squad_data['data']:
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            for qa in paragraph['qas']:
                question = qa['question']
                simplified_data.append({"context": context, "question": question})

    write_simplified_file(output_file, simplified_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert SQuAD-format JSON file to simplified JSON file with context and questions only.")
    parser.add_argument('--input_file', type=str, default="merged_dataset.json", help="Path to the input SQuAD-format JSON file.")
    parser.add_argument('--output_file', type=str, default="simplified_dataset.json", help="Path to the output simplified JSON file.")

    args = parser.parse_args()

    convert_squad_to_simplified(args.input_file, args.output_file)
