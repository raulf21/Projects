from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from selenium import webdriver
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,es;q=0.8,bs;q=0.7"
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers=headers)

data = response.text
soup = BeautifulSoup(data,'html.parser')

link_elements = []
for link in soup.find_all('a', {"class": "property-card-link"}):
    href = link.get("href")
    if not href.startswith('http'):
        link_elements.append(f"https://www.zillow.com{href}")
    else:
        link_elements.append(href)
address_elements = soup.select('.property-card-data address')
all_address = [address.get_text().split(" | ")[-1] for address in address_elements]

price_elements = soup.select('.property-card-data span')
all_prices = [price.get_text().split('+')[0].split('/mo')[0] for price in price_elements]

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

for n in range(len(link_elements)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScP7tk1zDAkZDWGj7kpBOyoenNnRA2WlrKLlWsi33u72IdDEw/viewform?usp=sf_link")
    time.sleep(5)

    address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    sumbit_button = driver.find_element(By.XPATH,'//div[@role="button"]')

    address.send_keys(all_address[n])
    price.send_keys(all_prices[n])
    link.send_keys(link_elements[n])
    sumbit_button.click()

driver.quit()