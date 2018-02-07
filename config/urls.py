"""MyBlogProject URL Configuration

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
# import django
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from apps.blog import views as blogviews

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', blogviews.IndexView.as_view(), name='index'),
    url(r'^index', blogviews.IndexView.as_view(), name='index'),
    # url (r'^index', blogviews.listing, name='index'),

    url(r'^myblog', blogviews.MyBlogView.as_view(), name='myblog'),

    url(r'^about', blogviews.about, name='about'),

    url(r'^write', blogviews.ArticleEditView.as_view(), name='write'),

    # 博客主页
    url(r'', include('apps.blog.urls')),

    # 认证系统相关的网页，用于注册，登录，修改密码和重置密码。
    url(r'', include('apps.blogauth.urls')),
    url(r'', include('django.contrib.auth.urls')),

    # 博客评论页面
    url(r'', include('apps.comments.urls')),
    # 记得在顶部引入 AllPostsRssFeed
    # url (r'^all/rss/$', AllPostsRssFeed (), name='rss'),


    url(r'^search/', include('haystack.urls')),

    # 增加markdownx
    url(r'^markdownx/', include('markdownx.urls')),

    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(如果符合这样规律的url，就去这个目录中找文件),没写找不到media_root中的媒体图片文件啊
