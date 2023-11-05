import gensim
import os
import string
import nltk, re, pprint

from nltk import wordpunct_tokenize

all_Texts = []
raw_directory_path = "C:/Users/theob/Code/PrivacyLLM/Privacy-LLM/Datasets/Natural Language/"

#tokenize a file
def PreProccesor(file):
    #read the raw file text
    raw = file.read()
    #tokenize
    tokens = nltk.wordpunct_tokenize(raw)
    #create and return a Text object with the tokens
    text = nltk.Text(tokens)
    return text

for file in os.listdir("C:/Users/theob/Code/PrivacyLLM/Privacy-LLM/Datasets/Natural Language/"):
    file_path = os.path.join(raw_directory_path, file)
    with open(file_path, 'r', encoding='utf-8') as file:
        all_Texts.append(PreProccesor(file))

print(all_Texts)