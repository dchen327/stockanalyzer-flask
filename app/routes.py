from flask import render_template, request
from app import app
from app.ticker_analyzer import ticker_analyzer


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['ticker']
        score = ticker_analyzer(text)
        return render_template('index.html', score=score, ticker=text)
    else:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
