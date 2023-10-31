import torch
from torch.utils.data import Dataset
import os

class CharDataset(Dataset):
    def __init__(self, text, seq_length):
        self.text = text
        self.seq_length = seq_length
        self.chars = sorted(list(set(text)))
        self.char_to_idx = {ch: i for i, ch in enumerate(self.chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(self.chars)}

text_data = []

for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r'):
            if file.endswith(".txt"):
                        file_path = os.path.join(file_path, file)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_text = file.read()
                            text_data += file_text

dataset = CharDataset(text_data, 10000)
print(dataset.chars)