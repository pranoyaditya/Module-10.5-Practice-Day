from django.shortcuts import render
from datetime import datetime

# Create your views here.
def lengthPractice(request):
    context = {
        'array' : [1,3,4,6,2,6],
    }

    return render(request, 'first_app/length.html', context)

def addPractice(request):
    context = {
        'number' : 5,
        'first_name': 'Sakurako',
        'last_name': 'Alex'
    }
    return render(request, 'first_app/add.html', context)

def addSlacesPractice(request):
    context = {
        'sentence' : "I'm Pranoy."
    }
    return render(request, 'first_app/addSlaces.html', context)

def capFirstPractice(request):
    context = {
        'sentence' : "my name is Pranoy."
    }
    return render(request, 'first_app/capFirst.html', context)

def curPractice(request):
    context = {
        'sentence' : "my name is Pranoy."
    }
    return render(request, 'first_app/cut.html', context)

def dictSortPractice(request):
    context = {
        'people' :
        [ 
            {'name': 'Abhi', 'age': 29},
            {'name': 'Rahul', 'age': 36},
            {'name': 'Sonia', 'age': 25},
        ]
    }
    return render(request, 'first_app/dictsort.html', context)

def escapePractice(request):
    context = {
        'sentence' : '<p>This <em>should be</em> fun!</p>'
    }
    return render(request, 'first_app/escape.html', context)

def firstPractice(request):
    context = {
        'lst': ['apple', 'banana', 'strawberry', 'mango']
    }
    return render(request, 'first_app/first.html', context)

def lastPractice(request):
    context = {
        'lst': ['apple', 'banana', 'strawberry', 'mango']
    }
    return render(request, 'first_app/last.html', context)

def lineNumbersPractice(request):
    context = {
    'names': "Arnold\nBrandy\nCaleb\nDexter"
    }
    return render(request, 'first_app/lineNumbers.html', context)

def lowerPractice(request):
    context = {
    'sentence': "Sakurako AND Alex ARE PLAYING A GAME."
    }
    return render(request, 'first_app/lower.html', context)

def upperPractice(request):
    context = {
    'sentence': "sakurako and alex are playing a game."
    }
    return render(request, 'first_app/upper.html', context)

def titlePractice(request):
    context = {
    'sentence': "sakurako and alex are playing a game."
    }
    return render(request, 'first_app/title.html', context)

def randomPractice(request):
    context = {
        'lst' : ['mango', 'banana', 'car', 'helicopter']
    }
    return render(request, 'first_app/random.html', context)

def dateTimePractice(request):
    context = {
        'dateTime' : datetime.now()
    }
    return render(request, 'first_app/dateTime.html', context)