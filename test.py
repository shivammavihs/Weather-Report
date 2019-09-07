import requests
import bs4
res = requests.get('https://www.timeanddate.com/weather/india').text
soup = bs4.BeautifulSoup(res,'html.parser')
for i in soup.find_all('p'):
    for j in i.find_all('span',class_='four'):
        print(i.text)

input('Press any key to exit')