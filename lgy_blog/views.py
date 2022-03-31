import markdown
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.template import loader

from lgy_blog.models import Blog
from lgy_blog.models import BlogType

from .forms import BlogPostForm
from django.contrib.auth.models import User

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
        blog_detail.blog_text = markdown.markdown(
            blog_detail.blog_text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
    except Blog.DoesNotExist:
        raise Http404(u'页面不存在')

    return render(request,'detail_page.html',{'blog_detail': blog_detail, 'type_list': BlogType})


def cover(request):
    return render(request,'cover.html')


#单独的about页面，放一些个人信息
def about(request):
    return render(request,'about_me.html')

#显示所有的type
def show_by_type(request):
    context = {'type_list': BlogType}
    return render(request, 'show_by_type.html', context)

#依照type把这些相关的博客筛选出来展示列表
def show_by_one_type(request,type_index):
    try:
        blog_list_type = Blog.objects.filter(blog_type=type_index)
    except Blog.DoesNotExist:
        raise Http404(u'页面不存在')
    return render(request, 'show_by_one_type.html', {'blog_list_type': blog_list_type})

#单独的搜索页
def search(request):
    pass


# 前端写文章的view
def blog_create(request):
    if request.method == 'POST':
        blog_post_form = BlogPostForm(data=request.POST)

        if blog_post_form.is_valid():
            new_blog = blog_post_form.save(commit=False)

            new_blog.creator = User.objects.get(id=1)

            new_blog.save()

            return redirect('/index')
        else:
            return HttpResponse("表单有误，请重新填写")

    else:
        blog_post_form = BlogPostForm()

        context = {'blog_post_form': blog_post_form}

        return render(request, 'new_blog.html', context)
