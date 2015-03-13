import urllib2
from bs4 import BeautifulSoup

url = "http://www.uniraq.org/index.php?option=com_k2&view=item&id=3344:un-casualty-figures-for-february-2015&Itemid=633&lang=en"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

with open('output.csv', 'w') as f:
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        f.write("%s, %s, %s\n" % \
              (tds[0].text, tds[1].text, tds[2].text))