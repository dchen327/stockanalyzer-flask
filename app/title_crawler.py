'''
Simple Python script that fetches RobinHood article names for stock tickers

Author: Daniel Li
'''

import requests
from bs4 import BeautifulSoup


def fetch_article_titles(ticker):
    try:
        # gets raw article data
        url = f'https://robinhood.com/stocks/{ticker}'
        article = requests.get(url, timeout=5)
        article_content = BeautifulSoup(article.content, "lxml")
        # hardcoded to find article titles specific to RobinHood; uses unique tags
        titles = article_content.find_all(
            "h3", class_="_1mENhHqLzNE3Fc8Lm0t1of")
        # sometimes it returns a None article title, idk why
        news_titles = [title.text for title in titles if title.text is not None]
        if news_titles == []:  # no titles found
            news_titles.append(f'No articles found for ticker {ticker}')
        return news_titles
    except Exception as e:
        print(e)


if __name__ == '__main__':
    ticker = 'AMZN'
    titles = fetch_article_titles(ticker)
    for title in titles:
        print(title)
