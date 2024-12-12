from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-published_date')  # Corrected line
    return render(request, 'news/news_home.html', {'news': news})

#12 Dec