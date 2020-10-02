import requests

url = "https://joke3.p.rapidapi.com/v1/joke"

headers =  {
    'x-rapidapi-host': "joke3.p.rapidapi.com",
    'x-rapidapi-key': "d00d113365mshea9eb74ea44fad6p110641jsn058c3c4b9deb"
}

response = requests.get(url, headers=headers)

joke = response.json()
print(joke)