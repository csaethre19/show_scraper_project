from django.shortcuts import render
from show_scraper_app.scraper import scrape

def home(request):
    return render(request, 'show_scraper_app/index.html')


def results(request, artists: str):
    artists = artists.split(',')
    concert_data = scrape(artists)
    return render(request, 'show_scraper_app/results.html', {'results' : concert_data})