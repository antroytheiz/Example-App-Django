from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'About',
        'page':'Salupa',
        'nav': [
            ['/','Home'],
            ['/about','About'],
        ]
    }
    return render(request,'home.html',context)