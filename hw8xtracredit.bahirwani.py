import urllib2
import json
import oauth2
from operator import itemgetter, attrgetter, methodcaller

# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = 'fOakpV5xYztpUWSwmNJ1bA'
CONSUMER_SECRET = 'DddxIR2AAUo5ivt5j4JSUXdTZlg'
TOKEN = 'jhrCPbC7obw49yYQAvTJu9MYbsQJ5Xxv'
TOKEN_SECRET = '8uPlD4GHliD2G338f57z08bf44M'

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

#################################################################################
# Your code goes here
restfile = open('restaurants2.bahirwani.txt', 'w')
JResponse = yelp_req('http://api.yelp.com/v2/search?term=restaurants&location=San+Francisco&limit=20')
#print JResponse[u'businesses'][0][u'name'], "####",int(JResponse[u'businesses'][0][u'review_count'])
arrayRest = [["",0] for i in range(40)]
#bNames=JResponse[2]
#print bNames
for i in range(20):
	arrayRest[i]=[JResponse[u'businesses'][i][u'name'].encode("utf-8"),JResponse[u'businesses'][i][u'review_count']]#          .businesses[i].name, JResponse.businesses[i].review_count]
	
	

JResponse = yelp_req('http://api.yelp.com/v2/search?term=restaurants&location=San+Francisco&limit=20&offset=20')
for i in range(20,40):
	arrayRest[i]=[JResponse[u'businesses'][i-20][u'name'].encode("utf-8"),JResponse[u'businesses'][i-20][u'review_count']]
	
for i in range(40):
	print arrayRest[i]

arrayRestSorted=sorted(arrayRest, key=itemgetter(1))
#print arrayRestSorted
for item in arrayRestSorted:
	restfile.write(item[0]+","+str(item[1])+"\n")	