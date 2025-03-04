from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Prefetch, F
from .models import Blog, Entry, Author


# Create your views here.

def main(request):
    return HttpResponse('<h1>Hello World</h1>')

def auto(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return HttpResponse(f'BLOG ID {blog}')

def index(request):
    latest_question = Blog.objects.order_by('-name')[:5]
    context = {'latest_question': latest_question}
    return render(request, 'polls/index.html', context)

def blog_author(request):
    # blogs = Blog.objects.annotate(authors=Count('author')).values('authors')
    blogs = Blog.objects.prefetch_related(
        Prefetch('entry_set', queryset=Entry.objects.all(), to_attr='entries')
    )
    context = {'blogs': blogs}

    return render(request, 'polls/second.html', context)