from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)

url = "https://uifaces.co/api?limit=5"

# querystring = {"location":"de","registrar":"dnsimple.com","defaults":"club%2Ccoffee","query":"acme cafe"}

headers = {
    'X-API-KEY': "10B30A17-B65D468A-913ABEED-7E36BEB8",
    'Accept': 'application/json',
	'Cache-Control': 'no-cache'
    }


@app.route('/')
def index():
    response = requests.get(url)

    domains = response.json()
    print(domains)
    return render_template('index.html', domains=domains)



if __name__ == "__main__":
    app.run(debug=True)