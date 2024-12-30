from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': "My name is Maksym and it's my first Django project"
    }
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, "main/contacts.html")