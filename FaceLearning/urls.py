"""FaceLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from FaceDetandRec import views

from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

#用于扫描并加载css、js等文件
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    #主页管理
    url(r'^home/$', views.home, name='home'),
    # url(r'^human/$', views.human, name='human'),
    # url(r'^animal/$', views.animals, name='animals'),
    # url(r'^others/$', views.others, name='others'),
    url(r'^history/$', views.history, name='history'),
    url(r'^history/home.*$', views.home, name='home'),
    # url(r'^history/history.*/$', views.home, name='home'),
    #图片管理
    url(r'^uploadImg/$', views.uploadImg, name='uploadImg'),
    url(r'^showImg/$', views.showImg, name='showImg'),
    # url(r'^FaceDetandRec/media/(?P<path>.*)$', serve, {'document_root': '/FaceLearning/media/imgOri'}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #用户认证
    url(r'^users/', include('FaceDetandRec.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
