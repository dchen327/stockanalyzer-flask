"""
The TitleCrawler class provides methods to grab article titles on Robinhood
relating to a provided stock ticker.
"""
import requests
from bs4 import BeautifulSoup


class TitleCrawler:

    def fetch_article_titles(self, ticker):
        """
        Given a stock ticker, return a list of article titles from Robinhood.
        Will return an empty list if no articles found (e.g. invalid ticker)
        """
        url = f'https://robinhood.com/stocks/{ticker}'  # url with info
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.content, 'lxml')
        # hardcoded to find article titles specific to RobinHood; uses unique
        # tags
        titles = soup.find_all(
            'h3', class_='_1mENhHqLzNE3Fc8Lm0t1of')
        # sometimes returned article title is None
        news_titles = [
            title.text for title in titles if title.text is not None]

        return news_titles


if __name__ == '__main__':
    ticker = 'AMZN'
    title_crawler = TitleCrawler()
    titles = title_crawler.fetch_article_titles(ticker)
    for title in titles:
        print(title)
