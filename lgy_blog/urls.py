from lgy_blog import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path("index/", views.index,name=u'索引页'),
    path("blog/<int:blog_id>/",views.detail_page, name=u'详情页'),
    #url(r"^blog/(?P<blog_id>\d)/$", views.detail_page, name=u'详情页'),
    path("about_me/", views.about, name=u'关于我'),
    path("type/<int:type_index>", views.show_by_one_type, name=u'分类详情'),
    path("type_list/", views.show_by_type, name=u'分类列表'),
    path("",views.cover,name=u'初始页'),
    path('blog-create/', views.blog_create, name=u'提交博客'),
    path('blog-safe-delete/<int:blog_id>/', views.blog_delete, name=u'删除博客'),
]

