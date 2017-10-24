"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

from .feeds import ArticleRssFeed

app_name = 'blog'

urlpatterns = [

    url(r'^$', views.MyBlogView.as_view(), name='index'),
    url (r'^index', views.MyBlogView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

    url (r'^testMarkdown', views.ArticleEditView.as_view (), name='testMarkdown'),

    # url(r'^search/$', views.search, name='search'),

    url(r'^rss/$', ArticleRssFeed(), name='rss'),

]

