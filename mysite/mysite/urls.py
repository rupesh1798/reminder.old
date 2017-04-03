"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from mysite.views import hello,home,time,hours_ahead,html,contact
from books import views
from reminder import rviews

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', time),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^html$',html),
#    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^meta/$', views.display_meta),
    url(r'^contact$', contact),
    url(r'^reminder$', rviews.reminder_home),
    url(r'^result$', rviews.reminder_result),
]
