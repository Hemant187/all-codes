

def speak(content):
    from win32com.client import Dispatch
    speak = Dispatch("sapi.spvoice")

    speak.Speak(content)
if __name__ == '__main__':
    import json
    import requests
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-02-28&sortBy=publishedAt&apiKey=d652c3c4d07b4315aa2ddf72d69a06b8'
    news = requests.get(url).text
    news_dict =json.loads(news)
    
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("moving on to the next news...listen")
    

