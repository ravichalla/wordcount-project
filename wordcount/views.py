from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')
def count(request):
	fulltext=request.GET['fulltext']
	words=fulltext.split()
	worddictionary={}
	for word in words:
		if word in worddictionary:
			worddictionary[word]+=1
		else:
			worddictionary[word]=1
	sortedWords=sorted(worddictionary.items(),key= operator.itemgetter(1),reverse=True)
	print(sortedWords)
	return render(request,'count.html',{'fulltext':fulltext,'words':len(words),'sortedWords':sortedWords})
