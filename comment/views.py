from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from lgy_blog.models import Blog
from .forms import CommentForm

# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = blog
            new_comment.user = request.user
            new_comment.save()
            return redirect('/blog/{}'.format(blog_id))
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")