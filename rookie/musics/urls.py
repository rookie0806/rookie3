from django.urls import path
from . import views
from django.conf.urls import url
app_name = "users"

urlpatterns = [
   url(
       regex=r'^top100/$',
       view=views.ListTop100.as_view(),
       name = 'view_top100'
   )
]