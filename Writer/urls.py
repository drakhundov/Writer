from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path("articles/", include("articles.urls")),
    path("polls/", include("polls.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
