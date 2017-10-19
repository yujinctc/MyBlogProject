"""Auth URL Configuration

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
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as authviews

app_name = 'blogauth'
urlpatterns = [

    url (r'^register/', views.register, name='register'),
    url (r'^register/', views.register, name='register'),


    #
    # # as别名的方式，引入了auth自带的
    url(r'^login/$', views.BlogLoginView.as_view(), name='login'),

    url(r'^logout/$', authviews.LogoutView.as_view(), name='logout'),

    url(r'^password_change/$', authviews.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', authviews.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/$', authviews.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', authviews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        authviews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', authviews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]