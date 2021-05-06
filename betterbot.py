import requests
import webbrowser
import datetime
import sys
import time
from bs4 import BeautifulSoup


sleepTime = 0 #seconds
audioUrl = '/home/tbartkowiak/Desktop/alert.ogg'

urlMap = {
    'Founder\'s Edition':'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    'EVGA XC3 ULTRA': 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6432400.p?skuId=6432400',
    'EVGA FTW3 GAMING': 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191'
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
}

while True:

    for urlKey in urlMap.keys():
        try:
            currentDateTimeStr = '{:%Y-%m-%d %H:%M:%S} |'.format(datetime.datetime.now())

            page = requests.get(urlMap[urlKey], headers=headers)

            soup = BeautifulSoup(page.content, 'html.parser')

            button = soup.find('button', class_='add-to-cart-button')
            buttonText = button.text

            if (buttonText.lower() != 'sold out' and buttonText.lower() != 'coming soon') :
                webbrowser.open(audioUrl, new= 1, autoraise= True)
                webbrowser.open(urlMap[urlKey], new= 2, autoraise= True)
                print(currentDateTimeStr, urlKey,' Found!, Opening web browser!')
                input('Press enter to continue search')
            else:
                print(currentDateTimeStr, 'No', urlKey, ' :(')
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(currentDateTimeStr, 'Ran into a fucky wucky.')

    time.sleep(sleepTime)