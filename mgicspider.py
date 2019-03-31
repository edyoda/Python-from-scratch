import requests 
from bs4 import BeautifulSoup

def generate_data(page_no):
    data = {
		"propertyType_new": "10002_10003_10021_10022",
		"city": 3327,
		"mbTrackSrc": "homeSearchForm",
		"searchType": 1,
		"propertyType": "10002,10003,10021,10022",
		"category": "S",
		"offset": 0,
		"maxOffset": 0,
		"page": page_no, 
    }
    return data
    
for index in range(1,11):
    print("**************Page {} *********".format(index))
    data = generate_data(index)
    response = requests.post("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore",data = data)
    soup = BeautifulSoup(response.content,"html.parser")
    
    cards = soup.find_all("div",attrs ={"class":"m-srp-card__container"})
    for card in cards:
        price = card.find("div",attrs ={"class":"m-srp-card__price"}) 
        title = card.find("a",attrs = {"class":"m-srp-card__title"})
        title_text = title.text.replace("\n"," ")
        area = card.find("div",attrs = {"class":"m-srp-card__summary__info"})
        if area:
        	area_text = area.text
        else:
        	area_text = None
        print("{} {} {}".format(title_text,area_text,price.text))
