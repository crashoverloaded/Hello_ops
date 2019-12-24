from bs4 import BeautifulSoup
import requests

url="http://coreyms.com"

# It will recieve response object or code
response=requests.get(url)

# Getting text out of that response
data=response.text
# Using Beautiful soup to parsing html webpage
# Here lxml parser is used
soup=BeautifulSoup(data,'lxml')

# it justs print out the html code recieved in a perfect manner
#print(soup.prettify())

for article in soup.find_all('article'):

#print(article.prettify()) 

	headline=article.h2.a.text
#print(headline)

	summary = article.find('div',class_='entry-content')
#print(summary.p.text)

	video = article.find('iframe',class_='youtube-player')['src']
#print(video)

	id=video.split('/')[4]
#print(id)
	id=id.split('?')[0]
#print(id)

	youtube_link=f"https://youtube.com/watch?v={id}"
	print(youtube_link)
	print("\n")




