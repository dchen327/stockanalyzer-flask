from flask import render_template, request
from app import app
@app.route('/',methods=['GET','POST'])

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        text = request.form['ticker']
        return render_template('index.html',ticker=text)
    else:
        return render_template('index.html')

    

