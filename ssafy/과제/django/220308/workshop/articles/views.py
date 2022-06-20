from email import contentmanager
from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):

    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # article = Article()
    # article.title = request.GET.get('title')
    # article.content = request.GET.get('content')

    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/create.html')