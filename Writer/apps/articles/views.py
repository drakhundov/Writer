from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article
from .forms import ArticleModel, CommentModel


def last(request):
    last_articles = Article.objects.order_by("-pub_date")[:5]
    context = {"last_articles" : last_articles}
    return render(request, "articles/last.html", context)


def detail(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except:
        raise Http404("Article Not Founded!")
    context = {"article" : article}
    return render(request, "articles/detail.html", context)


def new(request):
    return render(request, "articles/new.html")


def save(request):
    article = Article(title = request.POST["title"], text = request.POST["text"])
    article.save()
    return HttpResponseRedirect(reverse("articles:detail", args = (article.id,)))


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except:
        raise Http404("Article Not Founded!")
    comment = article.comment_set.create(author = request.POST["username"], text = request.POST["text"])
    comment.save()
    return HttpResponseRedirect(reverse("articles:detail", args = (article_id,)))
