import requests
from bs4 import BeautifulSoup
import smtplib

# Your email
EMAIL = ""
# Your password
PASS = ""
# Reciever email
RECIEVER_EMAIL = ""

# To provide USER_AGENT and ACCEPT_LAN, check the link below
# http://myhttpheader.com/
USER_AGENT = ""
ACCEPT_LAN = ""
# Product Link
PRODUCT_LINK = ""

headers = {
    "Accept-Language": ACCEPT_LAN,
    "User-Agent": USER_AGENT
}

response = requests.get(url=PRODUCT_LINK
                        , headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
product_name = soup.find(id="productTitle").getText()
p_name = ' '.join(product_name.split())
new_price = price.strip("$")

# set your price
my_price = 0

if my_price > float(new_price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECIEVER_EMAIL,
            msg=f"Subject: {p_name}\n\n The price for a product that you interested in {p_name} has reduced to {new_price}$, "
                f"you can visit your product via link below\n{PRODUCT_LINK}"
        )