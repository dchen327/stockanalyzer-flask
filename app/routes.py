from flask import render_template, request
from app import app
from app.ticker_analyzer import ticker_analyzer


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/sentiment.html', methods=['GET', 'POST'])
def sentiment():
    if request.method == 'POST':
        text = request.form['ticker']
        score = ticker_analyzer(text)
        return render_template('sentiment.html', score=score, ticker=text)
    else:
        return render_template('sentiment.html')


@app.route('/about.html')
def about():
    return render_template('about.html')
