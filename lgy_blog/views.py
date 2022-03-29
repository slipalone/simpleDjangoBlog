from django.http import Http404
from django.shortcuts import render
from django.template import loader

from lgy_blog.models import Blog
from lgy_blog.models import BlogType

#首页(附带展示bloglist的功能)
def index(request):
    blog_list = Blog.objects.order_by('created_date')
    # templates = loader.get_template('blog_list.html')
    context = {'blog_list': blog_list}

    for blog in blog_list:
        blog.blog_type = BlogType[blog.blog_type][1]

    return render(request, 'index.html', context)

#详情页
def detail_page(request, blog_id):
    try:
        blog_detail = Blog.objects.get(pk=blog_id)
        blog_detail.blog_type = BlogType[blog_detail.blog_type][1]
    except Blog.DoesNotExist:
        raise Http404(u'页面不存在')

    return render(request,'detail_page.html',{'blog_detail': blog_detail})


def cover(request):
    return render(request,'cover.html')


#单独的about页面，放一些个人信息
def about(request):
    return render(request,'about_me.html')

#显示所有的type
def show_by_type(request):
    pass

#依照type把这些相关的博客筛选出来展示列表
def show_list_by_type(request):
    pass

#单独的搜索页
def search(request):
    pass


