from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.\
BlogType = [
    (0,"技术类"),
    (1,"生活类"),
    (2,"家庭类"),
    (3,"爱好类")
]

'''
暂时不做标签的功能
class Tag(models.Model):
    tag_name = models.CharField(verbose_name=u'文章标签', max_length=20)

    class Meta:
        verbose_name = u'文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name
'''



class Blog(models.Model):
    blog_type = models.SmallIntegerField(blank=False, choices=BlogType, verbose_name=u'博客类型')
    blog_title = models.CharField(blank=False, max_length=250, verbose_name= u'博客标题', unique=True)
    blog_simple_text = models.CharField(blank=False, max_length=250, verbose_name= u'博客简介',help_text=u'请用简短的写一下本Blog的简述')
    blog_text = models.TextField(blank=False, max_length=2048, verbose_name= u'博客内容')
    creator = models.ForeignKey(User, verbose_name=u'创建人', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=u'创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=u'修改日期', default=datetime.now)
    click_nums = models.IntegerField(verbose_name=u'点击量',default=0)
    #tag = models.ManyToManyField(Tag, verbose_name=u'博客标签')

    class Meta:
        verbose_name = u'个人博客'
        verbose_name_plural = verbose_name
        ordering = ('-created_date',)

    def __str__(self):
        return self.blog_title





