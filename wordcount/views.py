from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'count':count, 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
