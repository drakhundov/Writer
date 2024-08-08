from django.forms import ModelForm, TextInput, Textarea

from .models import Article, Comment


class ArticleModel(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]

        widgets = {
            "title": TextInput(attrs={
                "class": "article-title",
                "placeholder": "Title"
            }),

            "text": Textarea(attrs={
                "class": "article-text",
                "placeholder": "Text"
            })
        }


class CommentModel(ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]

        widgets = {
            "author": TextInput(attrs={
                "placeholder": "UserName",
                "required": True,

                "name": "username"
            }),

            "text": Textarea(attrs={
                "placeholder": "Comment",
                "required": True,

                "cols": "30",
                "rows": "10",

                "name": "text"
            })
        }
