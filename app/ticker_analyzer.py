from app.sentiment_analyzer import SentimentAnalyzer
from app.title_crawler import TitleCrawler


def ticker_analyzer(ticker):
    """ Return an average sentiment and magnitude for a given stock ticker """
    title_crawler = TitleCrawler()
    titles = title_crawler.fetch_article_titles(ticker)
    if titles == []:
        return f'No articles found for {ticker}'
    analyzer = SentimentAnalyzer()
    scores = []
    for title in titles:
        score, magnitude = analyzer.analyze(title)
        scores.append(score * magnitude)  # interpretation of API output

    return f'{100 * sum(scores) / len(scores):.2f}'


if __name__ == '__main__':
    print(ticker_analyzer('AMZN'))
