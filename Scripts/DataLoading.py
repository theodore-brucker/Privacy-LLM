import torch
import torchtext
import os

def tokenize(label, line):
    return line.split()

tensors = []
tokens = []
directory = 'C:/Users/theob/Code/PrivacyLLM/Privacy-LLM/Datasets/Natural Language/'

#for each file in the target directory
for filename in os.listdir(directory):
    path = directory + filename
    NL = torch.utils.data.DataLoader(path, 100, shuffle=False)
    tensors += NL

for i, batch in enumerate(tensors): 
    print(i, batch) 

# for label,line in tensors:
#     tokens += tokenize(label,line)
# print(tokens)