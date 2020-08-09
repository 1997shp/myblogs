from django.contrib import admin
from .models import BlogType,Blog, ReadNum
# Register your models here.

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):

    #显示列表
    list_display = ('id','type_name')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('title','content','author','readed_num','created_time','last_updated_time')


# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):

#     #显示列表
#     list_display = ('blog')