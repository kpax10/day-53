from bs4 import BeautifulSoup
import requests

GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSep-Da6bRUT9yxqkIdZQ5mx1_V10lDX5YxZkrHQNodWT9NArw/viewform?usp=sharing&ouid=115047315612100414139'
ZILLOW_CLONE_SITE = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(ZILLOW_CLONE_SITE, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')

link_html = soup.find_all('a', class_='property-card-link', href=True)
links_text = [link['href'] for link in link_html]


