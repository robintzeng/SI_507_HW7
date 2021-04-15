from flask import Flask, render_template
import requests
import secrets


class Headline:
    def __init__(self, topic, url, thumbnails) -> None:
        self.topic = topic
        self.url = url
        self.thumbnails = thumbnails


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Welcome! </h1>'


@app.route('/name/<nm>')
def hello_name(nm):
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(
        secrets.api_key)
    headlines = requests.get(url).json()
    headline_obj_ls = []
    for i in range(5):
        h = headlines['results'][i]
        tmp = Headline(h['title'], h['url'], h['multimedia'][1]["url"])
        headline_obj_ls.append(tmp)
    return render_template('name.html', name=nm, headlines=headline_obj_ls)


if __name__ == '__main__':
    # url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(
    #     secrets.api_key)
    # headlines = requests.get(url).json()
    # headline_obj_ls = []
    # for i in range(1):
    #     h = headlines['results'][i]
    #     print(h['title'])
    #     print(h['multimedia'][1]["url"])
    #     print(h['url'])
    #     #tmp = Headline(h['title'], h['url'], h['thumbnail'])
    #     # headline_obj_ls.append(tmp)

    app.run(debug=True)
