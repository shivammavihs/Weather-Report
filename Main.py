import requests
import bs4
res = requests.get('https://www.timeanddate.com/weather/india').text
soup = bs4.BeautifulSoup(res,'html.parser')
cities,temps = [],[]
for city in soup.find_all('td'):
    if city.a != None: cities.append(city.a.text)
for temp in soup.find_all('td',class_='rbi'):
    temps.append(int(temp.text[0:2]))
data=dict(zip(cities, temps))
a = sorted(data.items(),key = lambda t:t[1])
print('Coolest city of India is {} with {} degrees\nHottest city of India is {}with {} degrees'.format(a[0][0],a[0][1],a[len(a)-1][0],a[len(a)-1][1]))

input('Press any key to exit')