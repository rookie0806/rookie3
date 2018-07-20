from django.urls import path
from . import views
from django.conf.urls import url
from rookie.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(r'^login/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
]
