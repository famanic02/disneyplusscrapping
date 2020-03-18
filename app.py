from flask import Flask
from flask import jsonify
from scrappy.disneyplus_scrape import DisneyPlusScrape

app = Flask(__name__)


@app.route('/')
def hello_world():
    obj = DisneyPlusScrape()
    m = obj.getData()
    return jsonify({'Sections': m})


if __name__ == '__main__':
    app.run()


