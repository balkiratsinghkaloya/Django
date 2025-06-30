import requests
from django.shortcuts import render

def home(request):
    news_list = []
    query = request.GET.get('query', 'technology')  # default query
    api_key = 'pub_358d6a6ce0d446029f4427aa6b6becb7'
    url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}&language=en'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        raw_news = data.get('results', [])
        for item in raw_news:
            news_list.append({
                'title': item.get('title'),
                'description': item.get('description'),
                'link': item.get('link'),
                'pubDate': item.get('pubDate'),
                'image_url': item.get('image_url', ''),  # sometimes empty
            })

    return render(request, 'newsapp/home.html', {'news_list': news_list, 'query': query})
