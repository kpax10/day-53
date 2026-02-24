from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re

GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSep-Da6bRUT9yxqkIdZQ5mx1_V10lDX5YxZkrHQNodWT9NArw/viewform?usp=sharing&ouid=115047315612100414139'
ZILLOW_CLONE_SITE = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(ZILLOW_CLONE_SITE, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')

links_html = soup.find_all('a', class_='property-card-link', href=True)
prices_html = soup.find_all(attrs={'data-test':'property-card-price'})
addresses_html = soup.find_all(attrs={'data-test': 'property-card-addr'})

links_text = [link['href'] for link in links_html]
prices_text = [re.split(r"[\/+]", price.text)[0] for price in prices_html]
addresses_text = [re.sub(r"^.*?[,/|]", "",address.text.rstrip().strip()) for address in addresses_html]

listings = zip(addresses_text, prices_text, links_text)


driver = webdriver.Chrome()
driver.get(GOOGLE_FORM_LINK)

address_input = driver.find_element(By.CSS_SELECTOR, '.whsOnd.zHQkBf')
address_input.send_keys('test')

# for listing in listings:
#   print(listing)



input('Press Enter to close....')