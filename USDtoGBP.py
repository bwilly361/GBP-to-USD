from bs4 import BeautifulSoup
import requests

#Get user GBP amount
user_amount = int(input("Enter amount of GBP you wish to convert: "))

#Scrape webpage
page_text = requests.get('https://www.exchangerates.org.uk/Pounds-to-Dollars-currency-conversion-page.html').text
soup = BeautifulSoup(page_text, 'lxml')


#Get price of USD in GBP
price = soup.find('td', class_ = 'convtop').text

price_num = price.split()[-2]

#convert price string to float
price_num_convert = float(price_num)

conversion = price_num_convert * user_amount

#format conversion to second decimal
conversion_formatted = "{:.2f}".format(conversion)

#print conversion
print("Your £" + str(user_amount) + " in GBP is equal to $" + str(conversion_formatted) + " in USD.")
