#importing things that we need for data scrapping
import bs4
import requests
import pandas as pd
import csv

#sending get data request to the target website
req = requests.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

#parsing the information
soup=bs4.BeautifulSoup(req.text, features='html.parser')

#creating list to store the info of all the items in a page
products=[]
prices=[]
ratings =[]

#getting the text of all the items using a loop 
for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})

    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

#creating the columns in the excel and saving the data from memory to local excel sheet
df = pd.DataFrame({"Product Name":products, "Price":prices, "Rating":ratings})
df.to_excel('Data.xlsx')