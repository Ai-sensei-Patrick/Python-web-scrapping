from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.sheads.com.au/buying/listings.php'

# opening up connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grab each product
containers = page_soup.find_all("article",{"class" : "col-md-4 col-sm-6 col-xs-12 listing listings_only"})

#create new file to write
filename = "property.csv"
f = open(filename, "w")
title = "Location, Suburb, Price, Bedroom, Bathroom, Car Park\n"
f.write(title)

for container in containers:
    Address = container.div.div.a.img["title"].strip().split(",")
    location = Address[0].strip()
    suburb = Address[1].strip()
    raw_price = container.find_all("p",{"class" : "price"})
    price = raw_price[0].text.strip().replace(",","")
    if price.startswith("-"):
        price = price.replace("-","").strip()
    raw_bedroom = container.find_all("span",{"class" : "ab-bed ab_bbc"})
    bedroom = raw_bedroom[0].text.strip()
    raw_bathroom = container.find_all("span",{"class" : "ab-bath ab_bbc"})
    bathroom = raw_bathroom[0].text.strip()
    raw_carpark = container.find_all("span",{"class" : "ab-car ab_bbc"})
    carpark = raw_carpark[0].text.strip()

    f.write(location + "," + suburb + "," + price + "," + bedroom + "," + bathroom + "," + carpark + "\n")
f.close()


