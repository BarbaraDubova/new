import requests


api_key = '8L9hk4ueCddGP7pFv2DJuV0YgsiwZpPcCu8WnY4Z'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'


response = requests.get(url)
   
if response.status_code == 200:
    data = response.json()
    print(f'Title: {data['title']}')
    print(f'Date: {data['date']}')
    print(f'URL: {data['url']}')
else:
    print('fail')
