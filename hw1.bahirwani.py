import getpass
pwd=None
while (pwd!="finish"):
	pwd=getpass.getpass('Enter a password to check for its strength or enter "finish" to end program: ')
	if pwd=="finish":
		break
	uppercondition=False
	lowercondition=False
	digitcondition=False
	charcondition=False
	lencondition=False
	countcondition=0
	for c in pwd:
		if c.isupper():
			uppercondition=True
		if c.islower():
			lowercondition=True
		if c.isdigit():
			digitcondition=True
		if c.isalnum()==False:
			charcondition=True
	if len(pwd)>5:
		lencondition=True
	if uppercondition==True and lowercondition==True:
		countcondition+=1
		print " It has at least one uppercase and at least one lowercase letter"
	else:
		print " It does NOT have at least one uppercase and at least one lowercase letter"
	if digitcondition==True:
		countcondition+=1
		print "It has at least one digit"
	else:
		print "It does NOT have at least one digit"
	if charcondition==True:
		countcondition+=1
		print " It has at least one character that is not a letter or a digit"
	else:
		print " It does NOT have at least one character that is not a letter or a digit"
	if lencondition==True:
		countcondition+=1
		print "It has a length of at least six characters"
	else:
		print "It does NOT have a length of at least six characters"
	print "-----------------"
	#print countcondition
	if countcondition==0:
		print "Your password is very weak"
	if countcondition==1:
		print "Your password is weak"
	if countcondition==2:
		print "Your password is medium strength"
	if countcondition==3:
		print "Your password is high medium strength"
	if countcondition==4:
		print "Your password is strong"
		
	pfile = open('common.txt', 'r')
	newpwd=pwd.lower();
	print newpwd
	pwdlist = []#defining a new list to store the passwords from the file
	for word in pfile:	
		pwdlist.append(word.rstrip())
	#print pwdlist
	lower=0
	upper=len(pwdlist)-1
	#itercount=0
	#found=False
	#below commented is the non-recursive implementation
	# while lower<upper-1 and found==False:
		# itercount+=1
		# mid=(lower+upper)/2
		# #print "Case 1 upper, lower and mid values are ", upper, lower, mid
		# if newpwd==pwdlist[mid]:
			# print "Note: Your password is common and number of turns it took to find is ", itercount
			# found=True
			# break
		# elif newpwd<pwdlist[mid]:
			# upper=mid
		# elif newpwd>pwdlist[mid]:
			# lower=mid
	# if found==False:
		# print "Your password is not found in the list of common passwords!"
	#print "The same results achieved below using recursive function as mentioned for extra credit part 2-------"
	def search(value, high_index,low_index):
		search.count+=1
		mid_index = (high_index+low_index)/2
		#print " Case 2 upper, lower and mid values are ", high_index, low_index, mid_index
		if high_index<=low_index+1:
			return False
		if value==pwdlist[mid_index]:
			return True
		elif value<pwdlist[mid_index]:
			return search(value,mid_index,low_index)
		elif value>pwdlist[mid_index]:
			return search(value,high_index,mid_index)
	#lower=0
	#upper=len(pwdlist)-1
	search.count=0
	if search(newpwd,upper,lower):
		print "Note: Your password is common and number of comparisons it took to find is ", search.count
	else :
		print "Note: Your password is not common"
	print "What is the relationship between this number and the size of the list?---- this number is basically the number of times the list had to be divided to find the value we were searching for"