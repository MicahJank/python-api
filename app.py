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
    # the pointe here is that i will just created a whole new list of posts
    # where each post contains just the information i need
    # i think this will be less messy than trying to scrape the html off
    # the posts and then update the original object
    updated_posts = []
    for post in posts:
        new_post = {}
        print(pprint.pprint(post))
        tree = html.fromstring(post['content'])
        content = tree.xpath('//*/text()')
        if len(content) > 0:
            new_post['content'] = content[0]
            new_post['title'] = post['title']
            new_post['url'] = post['url_for_post']
            new_post['tags'] = post['associated_topics']
            updated_posts.append(new_post)
            # post['content'] = content[0]
        
    # print(pprint.pprint(posts))
    # tree = html.fromstring(posts["posts"]["content"])
    # print(tree)
    return render_template('index.html', posts=updated_posts)



if __name__ == "__main__":
    app.run(debug=True)