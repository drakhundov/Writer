from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("last/", views.last, name = "last"),
    path("<int:article_id>/", views.detail, name = "detail"),
    path("new", views.new, name = "new"),
    path("save", views.save, name = "save"),
    path("<int:article_id>/leave_comment", views.leave_comment, name = "leave_comment"),
]