# -*- coding: utf-8 -*-
"""-------------------------------------------------
File Name:    urls.py
Description :
Author :       JHao
date:          2016/10/
------------------------------------------------
Change Activity:                   2016/10/10:
-------------------------------------------------
"""

from django.conf.urls import url
from article import views
urlpatterns = [
                url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
                url(r'^archives/$', views.archives, name='archives'),
                # url(r'^aboutme/$', 'article.views.aboutMe', name='about_me'),
                url(r'^tag/(?P<id>\d+)/$', views.category, name='category'),
                # url(r'^search/$', 'article.views.blogSearch', name='search'),
                url(r'.*?', views.home, name='home'),
              ]
