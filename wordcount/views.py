from django.http import HttpResponse
from django.shortcuts import render
import operator



def home(request):
    return render(request, 'home.html') #when you go to the home page, defined in urls,py, this tells you where to find that page
def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext'] #creates an object called fulltext received from the input in the word count box

    wordlist = fulltext.split() #counts the words, separating each word by a space

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords}) #adding the 'count' lets us know how many words are in our wordlist
