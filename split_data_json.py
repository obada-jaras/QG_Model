import json
from sklearn.model_selection import train_test_split

def clean_text(text):
    return text.replace("\t", " ").replace("\n", " ")

def squad_to_list(squad_data):
    data_list = []
    for article in squad_data:
        for paragraph in article['paragraphs']:
            context = clean_text(paragraph['context'])
            for qa in paragraph['qas']:
                question = clean_text(qa['question'])
                if len(qa['answers']) > 0:
                    answer = clean_text(qa['answers'][0]['text'])
                    if context and question and answer:
                        data_list.append({"context": context, "question": question})
    return data_list

def save_data_to_json(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_squad_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        squad_data = json.load(f)['data']
    return squad_data

input_file = "merged_dataset.json"
train_output_file = "train_qg.json"
valid_output_file = "valid_qg.json"

squad_data = load_squad_data(input_file)
train_data, valid_data = train_test_split(squad_data, test_size=0.2, random_state=42)

train_list = squad_to_list(train_data)
valid_list = squad_to_list(valid_data)

save_data_to_json(train_list, train_output_file)
save_data_to_json(valid_list, valid_output_file)

print(f"Number of items in train file: {len(train_list)}")
print(f"Number of items in valid file: {len(valid_list)}")
print(f"Total number of items: {len(train_list) + len(valid_list)}")
