#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23/023 23:41
# @Author : H
# @File : mycontextprocessor.py
from django.db.models import Count

from post.models import Post


def getRightInfo(request):

    # 1.获取分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    # 2.近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]

    # 3.获取归档信息，更具日期归档
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created ,count('*') as c FROM `t_post` GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c DESC,created DESC;")
    r_archive = cursor.fetchall()
    print(r_archive)

    return {"r_catepost":r_catepost,"r_recpost":r_recpost,"r_archive":r_archive}