"""
Created by 零柒叁 on 2019/7/30
"""

from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])