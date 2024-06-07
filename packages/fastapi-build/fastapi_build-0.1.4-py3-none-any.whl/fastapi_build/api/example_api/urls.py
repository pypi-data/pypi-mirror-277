# -- coding: utf-8 --
# @Time : 2024/6/6 10:40
# @Author : PinBar
# @File : urls.py
from . import APP_NAME
from core.base_view import path
from .example_view import ExampleView


urlpatterns = [
    path('/test', ExampleView, tags=[APP_NAME])
]