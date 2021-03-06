from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog , BlogType
from django.conf import settings
from datetime import datetime
each_page_blogs_number = 2
# Create your views here.

def get_blog_list_common_data(request,blogs_all_list):
    
    paginator = Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER) #每10篇进行分页
    page_num = request.GET.get('page',1)# 获取url页面参数GET请求
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  #获取当前页码
    page_range = list(range(max(current_page_num - 2 ,1), current_page_num))+list(range(current_page_num , min(current_page_num +2,paginator.num_pages) +1))
        #加上省略页码标记
    if page_range[0] -1 >=2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1]  >=2:
        page_range.append('...')
    
    # 加上首页和尾页
    if page_range[0] !=1 :
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

     


    context = {}

    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = Blog.objects.dates('created_time','month', order='DESC')
    return context

def blog_list(request):
    

    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request,blogs_all_list)
    return render_to_response('blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk = blog_pk)
    # if not request.COOKIES.get('blog_%s_readed' % blog_pk):

    blog.readed_num += 1
    blog.save()

    context = {}
    
    context['previous_blog'] = Blog.objects.filter(created_time__gt = blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt = blog.created_time).first()
    context['blog'] = blog
    response = render_to_response('blog/blog_detail.html',context) # 响应
    response.set_cookie('blog_%s_readed' % blog_pk,'true')

    return response


def blogs_with_type(request,blog_type_pk):


    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)

    context = get_blog_list_common_data(request,blogs_all_list)






    context['blog_type'] = blog_type

    return render_to_response('blog/blogs_with_type.html',context)


def blogs_with_data(request,year,month):
    # context = {}

    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    
    

    context = get_blog_list_common_data(request,blogs_all_list)
    context['blogs_wiht_date'] = '%s年%s月' % (year,month)

    return render_to_response('blog/blogs_with_date.html',context)