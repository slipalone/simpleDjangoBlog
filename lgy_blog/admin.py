from django.contrib import admin
from lgy_blog.models import Blog
#from lgy_blog.models import Tag
# Register your models here.

class blockAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('blog_type','blog_title','blog_text','creator','created_date','modified_date','click_nums')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Blog,blockAdmin)
#admin.site.register(Tag)