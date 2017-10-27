from django.db import models
from django.utils.six import python_2_unicode_compatible

from blog.models import Article
from blogauth.models import User


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255)
    # url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, blank=True)

    article = models.ForeignKey(Article, blank=True)

    author = models.ForeignKey(User, blank=True)

    def __str__(self):
        return self.text[:20]
