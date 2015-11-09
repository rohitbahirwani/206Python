#---------------------------------------------------------
# Rohit Bahirwani
# bahirwani.rohit@berkeley.edu
# Homework #3
# September 22, 2015
#---------------------------------------------------------
import string
import operator
from string import punctuation
import urllib2
# -------------------------
###############EXTRA Credit
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
print "###########################################################################"
print "The above list is created from the data fetched from the html file - EXTRA CREDIT implemented"
print "###########################################################################"
f.close()

###########################




catalogfile = open('catalog.txt')
Books = {}
Titles = []
i=0
for line in catalogfile:
	#line.rstrip()
	Titles.append(line[0: line.find(",") ])
	Books[line[0: line.find(",") ]] = [i, line[line.find(",")+1 : ].rstrip()]
	i+=1
#print "Books are    ",Books
# print "------------------"
# print Titles
Words = {}
i=0
# for entry in Books:
	
	# try:
		# url=str(Books[entry])
		# print "URL1 is ",url
		# url=url[url.find("'")+1:url.find("']")]
		# print "URL2 is ",url
		# response = urllib2.urlopen(url)
		# content = response.read()
		# for word in content.split():#txtfile.split():
			# word="".join([x for x in word if x.isalpha()])
			# word = word.lower()
			# if Words.has_key(word):
				# Words[word][i] += 1 
			# else:
				# Words[word] = []
				# for x in range(len(Books)):
					# Words[word].append(0)
				# Words[word][i] += 1
		# i+=1
	# except (urllib2.URLError):
		# #// terminate
		# print "There's a problem with the file or the URL"
		# exit()
		
		
for entry in Books:
	
	try:
		url=str(Books[entry])
		#print "URL1 is ",url
		url=url[url.find("'")+1:url.find("']")]
		#print "URL2 is ",url
		response = urllib2.urlopen(url)
		content = response.read()
		for word in content.split():#txtfile.split():
			word="".join([x for x in word if x.isalpha()])
			word = word.lower()
			if Words.has_key(word):
				Words[word][Books[entry][0]] += 1 
			else:
				Words[word] = []
				for x in range(len(Books)):
					Words[word].append(0)
				Words[word][Books[entry][0]] += 1
		i+=1
	except (urllib2.URLError):
		#// terminate
		print "There's a problem with the file or the URL"
		exit()	
	except :
		#// terminate
		print "Something went wrong, Please check back later. Or if you have checked assignments of too many people who implemented the Extra Credit, your Gutenberg Access may have been BLOCKED--pls check this assignment after 24 hours in that case."
		exit()
		

#url = "http://people.ischool.berkeley.edu/~tygar/for.i206/3cats1dog.txt"
#Optional (req = urllib2.Request(url))

#print Words

#txtfile = open('pg1342.txt')
#txtfile = txtfile.read().decode("utf-8-sig").encode("utf-8")
	#wordlist.append(word)
while True:
	searchWord = raw_input("Search term? ")
	if searchWord=="<terminate>":
		quit()
	elif searchWord == "<catalog>":
		for term in Books.items():
			print term
	elif searchWord == "<titles>":
		for term in Titles:
			print term		
	else:
		if Words.has_key(searchWord):
			# for item in Words[searchWord]:
				# if item==0:
	#---------------------------------			
			# #mydict = sorted(dict(zip(Titles,Words[searchWord])).values())
			# mydict = zip(Titles,Words[searchWord])
			# print "mydict1 is -------------",mydict, "type is ", type(mydict)
			# #mydict = sorted(mydict.items(),key=operator.itemgetter(1))
			# #mydict = dict(mydict)
			# mylist=sorted(mydict.items(), reverse=True)
			# print mylist[0]
			# del mydict
			# mydict = {}
			# for i in range(3):
				# a=str(mylist[i])[2:str(mylist[i]).find("',")]
				# b = int(str(mylist[i])[str(mylist[i]).find(",")+1 : str(mylist[i]).find(")") ])
				# mydict[a]=b
			# print "mydict2 is -------------",mydict
	#-------------------------------------------		
			# for i in sorted(mydict.keys(), reverse=True):
				# if mydict[i]!=0:
					# if mydict[i]>1:
						# print "The word ", searchWord,"appears ",mydict[i]," times in ",i, "link : ",Books[i][1]
					# else:
						# print "The word ", searchWord,"appears ",mydict[i]," time in ",i, "link : ",Books[i][1]
#---------------------------------------------
			# for i in mydict:
				# if mydict[i]!=0:
					# if mydict[i]>1:
						# print "The word ", searchWord,"appears ",mydict[i]," times in ",i, "link : ",Books[i][1]
					# else:
						# print "The word ", searchWord,"appears ",mydict[i]," time in ",i, "link : ",Books[i][1]
						
			templist=Words[searchWord]
			
			for i in range(len(Books)):
				max=0
				position=0
				for j in range (len(Books)):
					if templist[j]>max:
						max=templist[j]
						position=j
				if max!=0:				
					if max>1:
						print i+1,". The word ", searchWord,"appears ",max," times in ",Titles[position], " link : ",Books[Titles[position]][1]
					else:
						print i+1,". The word ", searchWord,"appears ",max," time in ",Titles[position], " link : ",Books[Titles[position]][1]
				templist[position]=0
						
			# for i in range(len(Books)):
				# print "i for searching is ",i
				# if Words[searchWord][i]!=0:	
					# print "Words[searchWord][i] is ----",Words[searchWord][i]
					# if Words[searchWord][i]>1:
						# print "The word ", searchWord,"appears ",Words[searchWord][i],"times in ",Titles[i], "link : ",Books[Titles[i]][1]
					# else:
						# print "The word ", searchWord,"appears ",Words[searchWord][i],"time in ",Titles[i], "link : ",Books[Titles[i]][1]
		else:
			print "The word ",searchWord," does not appear in any books in the library"