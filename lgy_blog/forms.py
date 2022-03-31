from django import forms

from .models import Blog

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ('blog_type', 'blog_title', 'blog_simple_text', 'blog_text')