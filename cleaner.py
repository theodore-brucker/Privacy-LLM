#cleaning HTML tags from files to get just the text from an HTML document

from bs4 import BeautifulSoup
import os

def remove_tags(html):
    # parse html content
    #soup = BeautifulSoup(html, "html.parser")
    soup = html
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

directory = 'C:/Users/theob/Code/PrivacyLLM/Privacy-LLM/Datasets/OPP-115_v1_0/OPP-115/sanitized_policies'
for filename in os.listdir(directory):
    fname = os.path.join(directory,filename)
    with open(fname, 'r') as f:
        soup = BeautifulSoup(f,'html.parser')
        # parse the html as you wish

        #remove the tags from the HTML doc and save it in a new variable
        cleaned_policy = remove_tags(soup)

        fileName = filename + '.txt'

        #write the clean policy to a new file using the name
        with open(fileName, 'w', encoding="utf-8") as f:
            f.write(cleaned_policy)