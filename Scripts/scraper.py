#Scraping random wikipedia articles and storing them in individual text files
import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url, breaker):
    #try:
    #Stop after 5th recursive call
    if(breaker == 500):
        exit()

    #Makes request to the url and parses into soup object
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    #Extract article title and body
    articleTitle = soup.find(id="firstHeading")
    articleText = "\n".join(p.text for p in soup.find_all("p"))

    fileName = articleTitle.text[0:10] + '.txt'

    #Write article body to a file named by the article title
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write(articleText)

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
    # except:
    #     scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping", breaker+1)

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping", 0)