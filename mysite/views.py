from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'page':'Salupa',
        'banner':'img/banner_home.png',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]

    }
    return render(request,'home.html', context)