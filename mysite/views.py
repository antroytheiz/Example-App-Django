from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'page':'Salupa',
        'nav':[
            ['/','Home'],
            ['/about','About'],
        ]

    }
    return render(request,'home.html', context)