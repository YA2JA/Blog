from django.shortcuts import render
from .models import Article



def home_page(request):
    article = Article.objects.order_by('id')[0] if len(Article.objects.order_by('id'))>0 else 'None'
    
    context = {
                'title':article._title,
                'content':article._content,
              }
    return render(request, 'publish/homePage.html', context)


def about_page(request):
    return render(request, 'publish/aboutPage.html')