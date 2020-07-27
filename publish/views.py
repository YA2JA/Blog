from django.shortcuts import render

def index(request):
    context ={
                "x":range(10),
            }
    return render(request, "publish/homePage.html", context)