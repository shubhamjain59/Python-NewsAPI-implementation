from newsapi import NewsApiClient
import requests

def Fetch_News_configure():
    newsapi = NewsApiClient(api_key ='0a72a4892b0a46ac96a52f057a8a19a5') 
    topnews = newsapi.get_top_headlines(q='startups',
                                        category='business',
                                        language='en', 
                                        country='in'
    )
    if topnews['status'] == 'ok':
        if topnews['totalResults'] == 0:
            return 'No results fetch'
        return topnews['totalResults']
    return 'Something wrong'

print(Fetch_News_configure())