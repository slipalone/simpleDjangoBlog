from lgy_blog import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r"^index/", views.index,name=u'主页'),
    url(r"^blog/(?P<blog_id>\d)/$", views.detail_page, name=u'详情页'),
    url(r'^about_me/', views.about, name=u'关于我'),
    path("",views.index,name=u'初始页'),

]

