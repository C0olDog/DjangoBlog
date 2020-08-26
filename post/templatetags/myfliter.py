#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23/023 21:32
# @Author : H
# @File : myfliter.py
from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)