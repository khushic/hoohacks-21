import requests
from bs4 import BeautifulSoup

def parse():
    URL = 'https://waset.org/research-conferences'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='eventList')
#print(results.prettify())
    events = results.find_all('li')
#print(events)
    arr = []
    for event in events:
        link = event.find('a')['href']
        title = event.find('a')['title']
        date = str(event).rfind('2021')
        year = 2021
        if date == -1:
            year= 2022
        new_event = {
            'link': link,
            'title': title,
            'year': year,
        }
        arr.append(new_event)
    for article in arr:
        try:
            Scraping.objects.create(
                title = article['title'],
                link = article['link'],
                year= article['year'],
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')
