import string
import operator
from string import punctuation
from bs4 import BeautifulSoup
htmlfile = open('Top 100 - Project Gutenberg.html')
soup = BeautifulSoup(htmlfile, 'html.parser')
headertag=soup.find(id="books-last1")
oltag=headertag.next_sibling.next_sibling
f = open('catalog.txt', 'w')
i=0
for link in oltag.find_all("a", limit=10):
	titlebook=link.text
	stringurlA=link.get('href')
	stringurlB=stringurlA[stringurlA.find("ebooks/")+7: ].strip()
	stringurlC=""+"http://www.gutenberg.org/files/"+stringurlB+"/"+stringurlB+"-h/"+stringurlB+"-h.htm"
	stringtowrite=(titlebook+","+stringurlC).encode("utf-8")
	if i<9:
		i+=1
		f.write(stringtowrite+"\n")
	else:
		f.write(stringtowrite)
	print(stringtowrite)
print "The above list is created from the data fetched from the html file"