from django.conf.urls import url, include
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^users/$', views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UsersDetail.as_view()),

    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),

    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
]

