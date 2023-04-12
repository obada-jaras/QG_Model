from torch.utils.data import Dataset, DataLoader
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = 't5-small'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def encode_input_target(context, answer, question, tokenizer):
    input_text = f"context: {context} answer: {answer}"
    target_text = question

    input_tokens = tokenizer.encode_plus(
        input_text,
        max_length=512,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )
    target_tokens = tokenizer.encode_plus(
        target_text,
        max_length=512,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    return input_tokens, target_tokens


class QGDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        context, answer, question = self.data[idx]
        input_tokens, target_tokens = encode_input_target(
            context, answer, question, self.tokenizer)
        return input_tokens, target_tokens


train_dataset = QGDataset(train_data, tokenizer)
val_dataset = QGDataset(val_data, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False)


class QGDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        context, answer, question = self.data[idx]
        input_tokens, target_tokens = encode_input_target(
            context, answer, question, self.tokenizer)
        return input_tokens, target_tokens


train_dataset = QGDataset(train_data, tokenizer)
val_dataset = QGDataset(val_data, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False)
