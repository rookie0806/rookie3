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
urlpatterns = [
   url(
       regex=r'^List/$',
       view=views.ListView.as_view(),
       name = 'List_View'
   ),
   url(
       regex=r'^feed/$',
       view=views.Feed.as_view(),
       name = 'Play_Lists'
   ),
   url(
       regex=r'^search/$',
       view=views.Search.as_view(),
       name = 'Search'
   )
]