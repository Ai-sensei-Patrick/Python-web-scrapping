from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.platypusshoes.com.au/shop/adidas'

# opening up connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grab each product
containers = page_soup.find_all("div",{"data-tb-sid" : "st_image-container"})

#create new file to write
filename = "shoes.csv"
f = open(filename, "w")
title = "brands, model, price\n"
f.write(title)

for container in containers:
    raw_brand = container.find_all("div",{"data-tb-sid" : "st_generic-link-wrapper"})
    brand = raw_brand[0].text.strip()
    brand_model = container.img["title"]
    raw_price = container.find_all("span",{"data-tb-sid" : "st_niceprice"})
    price = raw_price[0].text
    print(brand)
    print(brand_model)
    print(price)

    f.write(brand + "," + brand_model + "," + price + "\n")

f.close()