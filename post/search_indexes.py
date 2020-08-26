#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/24/024 23:17
# @Author : H
# @File : search_indexes.py

from haystack import indexes
from post.models import *


# 注意格式（PostIndex：模型类名+Index）
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title、content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
