from django.urls import path
from .views import home_page, about_page

names = ['', 'about', 'coucou', 'merch', 'Hello']

urlpatterns = [
   path('home', home_page, name = 'home'),
   path('about', about_page, name = 'about'),
   path('coucou', about_page, name = 'coucou'),
   path('merch', about_page, name = 'merch'),
   path('hello', about_page, name = 'hello'),
]