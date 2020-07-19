'''
Simple Python script that fetches RobinHood article names for stock tickers

by Daniel Li
'''

from bs4 import BeautifulSoup
import requests as rq
import argparse as ap

# takes an argument for the stock ticker and inserts it into the RobinHood URL
parser = ap.ArgumentParser()
parser.add_argument('-t', '--ticker', type=str, required=True,
                    help="Desired ticker to display article titles for")
args = vars(parser.parse_args())
ticker = args['ticker']
url = f'https://robinhood.com/stocks/{ticker}'


def fetch_article_titles(url):
    try:
        # gets raw article data
        article = rq.get(url, timeout=5)
        article_content = BeautifulSoup(article.content, "lxml")
        # hardcoded to find article titles specific to RobinHood; uses unique tags
        titles = article_content.find_all(
            "h3", class_="_1mENhHqLzNE3Fc8Lm0t1of")
        # sometimes it returns a None article title, idk why
        news_titles = [title.text for title in titles if title.text != None]
        return news_titles
    except:
        pass

if __name__ == '__main__':
    titles = fetch_article_titles(url)
    for title in titles:
        print(title)
