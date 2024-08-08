from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path("last/", views.last, name = "last"),
    path("<int:poll_id>/", views.detail, name = "detail"),
    path("<int:poll_id>/vote/", views.vote, name = "vote"),
    path("<int:poll_id>/results/", views.results, name = "results"),
]
