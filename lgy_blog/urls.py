from lgy_blog import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r"^index/", views.index,name=u'索引页'),
    url(r"^blog/(?P<blog_id>\d)/$", views.detail_page, name=u'详情页'),
    url(r'^about_me/', views.about, name=u'关于我'),
    url(r"^type_list/", views.show_by_type, name=u'分类列表'),
    path("",views.cover,name=u'初始页'),

]

