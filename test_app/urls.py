#coding:utf8
from django.conf.urls import url
from test_app.views import get_text, upload_text, index,success

urlpatterns = [
    url(r'^getText',get_text),
    url(r'^uploadText',upload_text),
    url(r'^success', success),
    url(r'^',index),
]