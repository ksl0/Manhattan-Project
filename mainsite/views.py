from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section, Article, Profile

def home(request):
    return render(request, 'index.html')

def section(request, section_name):
    articles = Section.objects.get(name=section_name).articles.all();
    return render(request, 'section.html', {"articles": articles});

def article(request, section_name, article_id, article_name='default'):
    article = Article.objects.get(pk=article_id);
    return render(request, 'article.html', {"article": article})

def person(request, person_id, person_name='ZQ'):
    person = Profile.objects.get(pk=person_id);
    if person.position == "author":
        articles = person.article_set.all();
        return render(request, 'author.html', {"articles": articles});
    if person.position == "photographer" or person.position == "graphic_designer":
        photographs = person.photo_set.all();
        return render(request, 'photographer.html', {"photographs": photographs});

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');