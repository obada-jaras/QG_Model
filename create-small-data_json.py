import json

def create_smaller_dataset(input_file, output_file, sample_size):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    smaller_data = data[:sample_size]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(smaller_data, f, ensure_ascii=False, indent=4)

train_input_file = "train_qg.json"
eval_input_file = "valid_qg.json"
train_output_file = "train_qg_tiny.json"
eval_output_file = "valid_qg_tiny.json"

create_smaller_dataset(train_input_file, train_output_file, 10)
create_smaller_dataset(eval_input_file, eval_output_file, 2)
