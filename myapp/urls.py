from django.urls import path, include
from . import views
from rest_framework import routers #routers allows get and post request
#get request shows something on the screen UI
#post request posts something to the database
router = routers.DefaultRouter()
router.register('books', views.BookView)#can change name of 'books' to anything we want
urlpatterns = [
    path('', include(router.urls)),
]

""" Old URL patterns before using rest
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
] """