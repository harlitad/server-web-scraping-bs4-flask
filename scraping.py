from bs4 import BeautifulSoup
import requests


def scrap():

    getData = requests.get(
        'http://mlg.ucd.ie/modules/COMP41680/assignment2/month-jan-001.html').text
    soup = BeautifulSoup(getData, "html.parser")
    # get all content inside class article, it will wrapped in an array object
    all_article = soup.find_all("div", {"class": "article"})

    # loop to get all the tag anchor and get the href attribute
    # for article in all_article:
    #     link = article.find('a')
    #     url = link.get('href')
    #     print(url)

    # loop using list generator
    return [article.find('a').get('href') for article in all_article]
