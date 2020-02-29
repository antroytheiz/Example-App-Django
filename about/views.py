from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'About',
        'page':'Salupa',
        'banner':'img/banner_about.png',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'home.html',context)