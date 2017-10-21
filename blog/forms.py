from django.forms import forms, models
from markdownx.fields import MarkdownxFormField

from blog.models import Article


class MyForm(forms.Form):
    myfield = MarkdownxFormField()


class ArticleForm(models.ModelForm):

    class Meta:
        model = Article
        fields = ('title','excerpt','body','category')