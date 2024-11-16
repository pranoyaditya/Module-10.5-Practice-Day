from django.urls import path
from . import views

urlpatterns = [
    path('length/', views.lengthPractice),
    path('add/', views.addPractice),
    path('addSlaces/', views.addSlacesPractice),
    path('capFirst/', views.capFirstPractice),
    path('cut/',views.curPractice),
    path('dictsort/', views.dictSortPractice),
    path('escape/', views.escapePractice),
    path('first/', views.firstPractice),
    path('last/', views.lastPractice),
    path('lineNumbers/', views.lineNumbersPractice),
    path('lower/', views.lowerPractice),
    path('upper/', views.upperPractice),
    path('title/', views.titlePractice),
    path('random/', views.randomPractice),
    path('dateTime/', views.dateTimePractice),
]