# -- coding: utf-8 --
# @Time : 2024/5/24 14:41
# @Author : PinBar
# @File : urls.py
from . import APP_NAME
from .demo import DemoView
from core.base_view import path

urlpatterns = [
    path('/user', DemoView, tags=[APP_NAME])
]
