from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect

from .models import Question


def last(request):
    last_polls = Question.objects.order_by("-pub_date")[:5]
    context = {"last_polls" : last_polls}

    return render(request, "polls/last.html", context)


def detail(request, poll_id):
    try:
        poll = Question.objects.get(id = poll_id)
    
    except:
        raise Http404("Question Not Founded!")


    context = {"poll" : poll}
    return render(request, "polls/detail.html", context)


def vote(request, poll_id):
    try:
        poll = Question.objects.get(id = poll_id)
    
    except:
        raise Http404("Poll Not Founded!")
    
    try:
        choice = poll.choice_set.get(id = request.POST["choice"])
        choice.votes += 1
        choice.save()
    
    except:
        raise Http404("Choice Not Founded!" + request.POST["choice"])

    return HttpResponseRedirect(reverse("polls:results", args = (poll.id,)))


def results(request, poll_id):
    try:
        poll = Question.objects.get(id = poll_id)
    
    except:
        raise Http404("Poll Not Founded!")
    
    context = {"poll" : poll}
    return render(request, "polls/results.html", context)