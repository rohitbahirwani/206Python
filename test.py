#---------------------------------------------------------
# Rohit Bahirwani
# bahirwani.rohit@berkeley.edu
# Homework #2
# September 15, 2015
# test.py
# test
#---------------------------------------------------------
import string
from BST import *
from hw2 import *

T = BSTree()


txtfile = open('prideandprejudice.txt')
txtfile = txtfile.read().decode("utf-8-sig").encode("utf-8")
wordlist = []#defining a list to store the words from the file

for word in txtfile.split():
	for mark in string.punctuation:
		word=word.replace(mark,'')
	word = word.lower()
	T.add(word)
	#wordlist.append(word)
#T.inOrderPrint()
#print wordlist

# for line in txtfile:
	# for word in line.split():
		# for mark in string.punctuation:
			# word=word.replace(mark,'')
		# word = word.lower()
		# wordlist.append(word)
# print wordlist


# T.add("4")
# T.inOrderPrint()
while True:
	searchWord = raw_input("Query? ")
	if searchWord=="terminate":
		quit()
	elif searchWord == "stats":
		print "Total number of nodes in the tree is", T.NumberNodes, " and height is ",T.height()
	else:
		T.find(searchWord)