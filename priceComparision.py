import requests
from bs4 import BeautifulSoup

keyword = input('Enter your product :')

urlA = 'https://www.amazon.in/s?k='+keyword+''
urlF = 'https://www.flipkart.com/search?q='+keyword+''
urlR = 'https://www.reliancedigital.in/search?q='+keyword+''

urlH = 'https://www.happimobiles.com/mobiles/all?serach=&q='+keyword+''
urlL = 'https://www.lotmobiles.com/catalogsearch/result/?q='+keyword+''
urlP = 'https://www.paiinternational.in/SearchResults.aspx?search='+keyword+''
urlB = 'https://www.bajajelectronics.com/product/search?q='+keyword+''

prices = {}
def scrape(url):
    if url == urlF:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemF = soup.find_all('div', class_='_4rR01T')
            costF = soup.find_all('div', class_='_30jeq3 _1_WHN1')
            #print(itemF[0].text + " " + costF[0].text)
            costF = costF[0].text[1:]
            prices["Flipkart"] = costF
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Flipkart is not found')

    elif url == urlA:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemA = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
            costA = soup.find_all('span', class_='a-offscreen')
            #print(itemA[0].text + " " + costA[0].text)
            costA = costA[0].text[1:]
            prices["Amazon"] = costA
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from amazon is not found')

    elif url == urlR:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemR = soup.find_all('p', class_='sp__name')
            costR = soup.find_all('span', class_='sc-bxivhb cHwYJ')
            #print(itemR[0].text + " " + costR[0].text)
            costR = costR[0].text[1:]
            prices["Reliance"] = costR
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from reliance is not found')

    elif url == urlH:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemH = soup.find_all('a', class_='name')
            costH = soup.find_all('div', class_='p-c')
            #print(itemH[0].text + " " + costH[0].text)
            costH = costH[0].text[1:]
            prices["Happi Mobiles"] = costH
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Happi mobiles is not found')

    elif url == urlL:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemL = soup.find_all('a', class_='product-item-link')
            costL = soup.find_all('span', class_='price')
            #print(itemL[0].text+ " " + costL[0].text)
            costL = costL[0].text[1:]
            prices["Lot Mobiles"] = costL
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Lot mobiles is not found')

    elif url == urlB:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemB = soup.find_all('h3',class_='prodHeaderDesc mb10')
            costB = soup.find_all('h3', class_='prodPrice d-inline')
            #print(itemB[0].text+ " " + costB[0].text)
            costB = costB[0].text[1:]
            prices["Bajaj"] = costB
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Bajaj is not found')

def priceComparision():
    print(f'Showing results for : {keyword} in different sites')
    for item in prices.items():
        print(item[0],":",item[1])
        
if __name__ == '__main__':
    print('connecting to Flipkart.com')
    scrape(urlF)
    print('connecting to Amazon.in')
    scrape(urlA)
    print('connecting to Reliance')
    scrape(urlR)
    print('connecting to happi mobiles')
    scrape(urlH)
    print('connecting to Lot Mobiles')
    scrape(urlL)
    print('connecting to Bajaj Electronics')
    scrape(urlB)
    priceComparision()
