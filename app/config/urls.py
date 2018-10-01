"""config URL Configuration

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
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    # name속성 : url에 이름을 붙임 -> 다른 영역에서 name을 이용해서 동적으로 url을 참조한다.
    # url의 id는 템플릿에서 kwargs로 인자를 넘겨줄 때의 이름.
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/$', views.post_list, name='post_list'),
]
