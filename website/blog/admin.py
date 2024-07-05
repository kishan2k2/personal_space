from django.contrib import admin

# Register your models here.
from blog.models import Category, Post, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)