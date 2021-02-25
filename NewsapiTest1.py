from newsapi import NewsApiClient
import requests

def Fetch_News_configure():
    newsapi = NewsApiClient(api_key ='0a72a4892b0a46ac96a52f057a8a19a5') 
    topnews = newsapi.get_top_headlines(q='bitcoin',
                                        language='en', 
                                        country='us'
    )
    if topnews['status'] == 'ok':
        if topnews['totalResults'] > 0:
            articleList = topnews['articles']
            for article in articleList:
                articleTitle = article['title']
                articleUrl = article['url']
                articleContent = article['content']
                return articleTitle, articleUrl, articleContent
            
            
        else:
            return "No Articles found related to this query. Please try another."
#articles -
    #source
    #author
    #title
    #url
    #urlToImage
    #publishedAt
    #content
    

print(Fetch_News_configure())