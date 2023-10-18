#Scraping random wikipedia articles and storing them in individual text files

import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url, breaker):
    
    #Stop after 5th recursive call
    if(breaker == 100):
        exit()

    #Makes request to the url and parses into soup object
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    #Extract article title and body
    articleTitle = soup.find(id="firstHeading")
    articleBodyStep = soup.body
    articleBody = ''
    for string in articleBodyStep.strings:
        articleBody += string

    fileName = articleTitle.text + '.txt'

    #Write article body to a file named by the article title
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write(articleBody)

    #Randomly select new wikipedia article to jump to
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1: 
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    #Recursive call with the new random link
    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'], breaker+1)

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping", 0)