from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]

"""
This part ^post/(?P<pk>\d+)/$ looks scary, but no worries – we will explain it for you:

it starts with ^ again – "the beginning".
post/ just means that after the beginning, the URL should contain the word post and a /. So far so good.
(?P<pk>\d+) – this part is trickier. It means that Django will take everything that you place here and transfer it to a view as a variable called pk. \d also tells us that it can only be a digit, not a letter (so everything between 0 and 9). + means that there needs to be one or more digits there. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK!
/ – then we need a / again.
$ – "the end"!
"""