from django.shortcuts import render
from .models import Comment


def blog_index(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    context = {
        'comment': comment
    }
    return render(request, 'blog_detail.html', context)