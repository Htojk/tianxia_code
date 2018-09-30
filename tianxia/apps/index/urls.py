#@Author   ：Htojk
#@Time     :2018/9/27  19:12
#@Software :PyCharm

from django.conf.urls import url
from .  import views

urlpatterns = [
    url(r'^$',views.Index_view,name='index')
]