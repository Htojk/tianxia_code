#@Author   ：Htojk
#@Time     :2018/9/27  19:12
#@Software :PyCharm

from django.conf.urls import re_path
from .  import views

app_name='users'
urlpatterns = [
    re_path(r'^$',views.Index_view,name='index'),
    re_path(r'^login/$',views.Login_view,name='login'),
    re_path(r'^logout/$',views.Logout_view,name='logout'),
    re_path(r'^register/$',views.Register_view,name='register'),
    re_path(r'^user_center/$',views.User_center_view,name='user_center'),
    # re_path(r'^artical_test/$',views.Artical_test_view,name='artical_test'),
    re_path(r'^pictures_show/(\d)/$',views.Pictures_show_details_view,name='pictures_show_details'),
    re_path(r'^changeMessage/$',views.Change_user_message_view,name='change_user_message'),
    re_path(r'^changePassword/$',views.Change_password_view,name='change_password'),
]