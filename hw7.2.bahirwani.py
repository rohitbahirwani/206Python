import itertools

ListOfNumbers=[]
a = list(itertools.product(range(100,1000),range(100,1000)))
b = map(lambda x:ListOfNumbers.append([x[0]*x[1],x[0],x[1]]),a)
Palindrome = filter(lambda x:str(x[0]) == str(x[0])[::-1],ListOfNumbers)
print max(Palindrome)