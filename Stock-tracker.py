def StockTracker():

    import requests
    from bs4 import BeautifulSoup

    url = input("Enter the yahoo finance URL of the stock you are looking for: ")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    return(price)

while True:
    print('Current Price of your stock is: ' +StockTracker())
