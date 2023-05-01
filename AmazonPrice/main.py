import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
EMAIL = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

ENDPOINT = "PRODUCT URL"

headers = {
    "User-Agent": #GET User-Agent FROM https://myhttpheader.com/,
    "Accept-Language":#GET Accept-Language FROM https://myhttpheader.com/,
    "Cookie":#GET COOKIE FROM https://myhttpheader.com/
}

response = requests.get(ENDPOINT,headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = float(price.split("$")[1])
print(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)


BUY_PRICE = 210

if price_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='RECIPIENT',
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{ENDPOINT}".encode("utf-8")
        )

