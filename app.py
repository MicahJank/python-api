from flask import Flask, render_template, url_for, redirect
import requests
import pprint
# lxml can help me scrape the data from the html
from lxml import html

app = Flask(__name__)

url = "https://api.dailysmarty.com/posts"

# querystring = {"location":"de","registrar":"dnsimple.com","defaults":"club%2Ccoffee","query":"acme cafe"}

# headers = {
#     'X-API-KEY': "10B30A17-B65D468A-913ABEED-7E36BEB8",
#     'Accept': 'application/json',
# 	'Cache-Control': 'no-cache'
#     }


@app.route('/')
def index():
    response = requests.get(url)

    posts = response.json()["posts"]
    content = ''

    for post in posts:
        tree = html.fromstring(post['content'])
        content = tree.xpath('//*/text()')
        if len(content) > 0:
            post['content'] = content[0]

        print(type(content))
        print(pprint.pprint(post))
        
    # print(pprint.pprint(posts))
    # tree = html.fromstring(posts["posts"]["content"])
    # print(tree)
    return render_template('index.html', posts=posts)



if __name__ == "__main__":
    app.run(debug=True)