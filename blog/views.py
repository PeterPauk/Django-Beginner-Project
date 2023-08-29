from django.shortcuts import render

posts = [
    {
        'author' : 'PeterPauk',
        'title' : 'The Industrial Revolution',
        'content' : 'Kinda bad ngl',
        'date_posted' : '29. August 2023'
    },

    {
        'author' : 'TheDarkOne',
        'title' : 'Masonic Rituals II',
        'content' : 'lets get into it',
        'date_posted' : '17. June 1987'
    },

    {
        'author' : 'Emonic',
        'title' : 'Esoteric Literature',
        'content' : 'we are going to pray tonight',
        'date_posted' : '31. September 2025'
    }
]

def home(request,):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

