from django.contrib import admin
from lgy_blog.models import Blog
#from lgy_blog.models import Tag
# Register your models here.

class blockAdmin(admin.ModelAdmin):
    # 非展示字段
    exclude = ('creator','created_date','modified_date')
    # 展示字段
    list_display = ('blog_type','blog_title','blog_text','creator','created_date','modified_date','click_nums')

    # 筛选条件
    list_filter = ('blog_type', 'creator', )

    # 查询字段
    search_fields = ('blog_title', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Blog,blockAdmin)
#admin.site.register(Tag)