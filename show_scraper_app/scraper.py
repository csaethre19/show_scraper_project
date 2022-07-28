import requests
from bs4 import BeautifulSoup

def scrape(artists: list[str]) -> dict:
    results = {}

    for artist in artists:
        url = 'https://google.com/search?q=' + artist + '+' + 'concert' + '+' + 'tickets'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a")
        show_links = []
        link_titles = []
        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                title = link.find_all('h3')
                link_titles.append(title)
                if len(title) > 0:
                    show_links.append(link.get('href').split('?q=')[1].split('&sa=U')[0])
        link_data = {
            'title' : link_titles,
            'links' : show_links
        }
        results[artist] = link_data

    return results



