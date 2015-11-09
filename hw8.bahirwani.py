import sys
import urllib
from bs4 import BeautifulSoup
import string
import operator
from operator import itemgetter, attrgetter, methodcaller

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code
# url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0#'
# content = urllib.urlopen(url).read()
# content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
# soup = BeautifulSoup(content)

# Your code goes here
restfile = open('restaurants.bahirwani.txt', 'w')
numRest = 40
arrayRest = [["",0] for i in range(numRest)]
dictRest={}
#print arrayRest
count=0
for i in range(0,numRest,10):
	url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start='+str(i)+'#'
	print url
	content = urllib.urlopen(url).read()
	content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
	soup = BeautifulSoup(content,"html5lib")
	startDivTag=soup.find("div", { "class" : "search-results-content" })
	"regular-search-result"
	divtags=startDivTag.findAll("div", { "class" : "search-result natural-search-result" })
	
	for j in divtags:
		aTitleTag=j.find("a", { "class" : "biz-name" })
		#print aTitleTag.text.encode("utf-8")
		spanReviewTag=j.find("span", { "class" : "review-count rating-qualifier" })
		#print spanReviewTag.text.encode("utf-8")
		dictRest[aTitleTag.text.encode("utf-8")]=spanReviewTag.text.encode("utf-8").replace(" reviews","")
		arrayRest[count]=[aTitleTag.text.encode("utf-8"),int(spanReviewTag.text.encode("utf-8").replace(" reviews",""))]
		count+=1

#print arrayRest

arrayRestSorted=sorted(arrayRest, key=itemgetter(1))
#print arrayRestSorted
for item in arrayRestSorted:
	restfile.write(item[0]+","+str(item[1])+"\n")		