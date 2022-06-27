#importing libraries.
import operator
from django.http import HttpResponse
from django.shortcuts import render
import operator
#Creating a function.
def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})
#Creating a function called count.
def count(request):
    """
        A function that handles a 
        user's request to go to a count page.
        
        Parameters: request.
    """
    #Grabbing the key of the parameter we are looking for.
    fulltext = request.GET['fulltext']
    #Splitting fulltext.
    wordlist = fulltext.split()
    #Creating a new dictionary.
    worddictionary = {}
    #Creating a for loop.
    for word in wordlist:
        #Checking if the word is in the dictionary.
        if word in worddictionary:
            #Incementing the word dictionary by 1.
            worddictionary[word] += 1
        #Handling the case where the word is not in the dictionary.
        else:
            #add the word to the dictionary.
            worddictionary[word] = 1
    #Turning the dictionary into a sorted list and assigning it to a variable.
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #Combining the given template with the context dectionary and returning HttpResponse with the rendered text.
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
#Creating a function to take the user to the about page.
def about(request):
    """
        A function that takes the user to the about 
        page and returns a HttpResponse with the rendered text.
        
        Args:
            request (_type_): _description_
    """
    return render(request, 'about.html')