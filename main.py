from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome() # options=chrome_options
driver.get(GOOGLE_FORM_LINK)

wait = WebDriverWait(driver,5)

for listing in listings:
  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

  address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  address_input.send_keys(listing[0])
  price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  price_input.send_keys(listing[1])
  link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
  link_input.send_keys(listing[2])
  submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
  submit.click()

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))

  reload_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
  reload_page.click()

driver.quit()