#---------------------------------------------------------
# Rohit Bahirwani
# bahirwani.rohit@berkeley.edu
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------


class Node:
	#Constructor Node() creates node
	def __init__(self,word):
		self.word = word
		self.right = None
		self.left = None
		self.count = 1

class BSTree:
	NumberNodes=0
	#Constructor BSTree() creates empty tree
	def __init__(self, root=None):
		self.root = root
	#These are "external functions" that will be called by your main program - I have given these to you =)
	#Find word in tree
	def find(self, word):
		return _find(self.root, word)
	
	#Add node to tree with word
	def add(self, word):
		if not self.root:
			self.root = Node(word)
			return
		_add(self.root, word)

	#Print in order entire tree
	def inOrderPrint(self):
		_inOrderPrint(self.root)

	def size(self):
		return _size(self.root)
	
	def height(self):
		return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
	if root.word == word:
		root.count += 1
		return
	if root.word > word:
		if root.left == None:
			root.left = Node(word)
			BSTree.NumberNodes+=1
		else:
			_add(root.left, word)
	else:
		if root.right == None:
			root.right = Node(word)
			BSTree.NumberNodes+=1
		else:
			_add(root.right, word)
			

#Function to find word in tree
def _find(root, word):
	found = False
	if root.word == word:
		found=True
		print "The word "+word+" appears ",root.count," times in the tree"
		return
	elif (root.word > word):
		if (root.left is not None):
			_find(root.left, word)
	elif (root.word < word):
		if (root.right is not None):
			_find(root.right, word)
	# else:
		# print "This word was not found in the tree"
		# return
	# if found == False:
		# print "The word ", word, "was not found"
		# return

#Get number of nodes in tree
def _size(root):
	self.root = None

#Get height of tree
def _height(root):
	if root.left == None and root.right==None:
		return 0
	elif root.left == None and root.right != None:
		return 1+_height(root.right)
	elif root.left != None and root.right == None:
		return 1+_height(root.left)
	else:
		return 1+max(_height(root.left),_height(root.right))
    
#Function to print tree in order
def _inOrderPrint(root):
	if not root:
		return
	_inOrderPrint(root.left)
	print root.word
	print root.count
	_inOrderPrint(root.right)