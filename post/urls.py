#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23/023 19:56
# @Author : H
# @File : urls.py



from django.urls import path, re_path

from post import views


urlpatterns = [
    path('', views.queryAll),
    re_path(r'page/(\d+)',views.queryAll),
    re_path(r'post/(\d+)',views.detail),
    re_path(r'category/(\d+)',views.queryPostByCid),
    re_path(r'archive/(\d+)/(\d+)',views.queryPostByCreated),
]
