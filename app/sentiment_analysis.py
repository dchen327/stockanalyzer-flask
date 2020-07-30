from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class SentimentAnalyzer:

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def analyze(self, text):
        """ Return a tuple of sentiment score (-1, 1) and sentiment magnitude (0, inf) """
        self.document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT
        )
        sentiment = self.client.analyze_sentiment(document=self.document).document_sentiment
        return (sentiment.score, sentiment.magnitude)


if __name__ == '__main__':
    analyzer = SentimentAnalyzer()
    print(analyzer.analyze('Truly an amazing experience. I loved the atmosphere and the food.'))
