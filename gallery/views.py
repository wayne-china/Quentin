#!/usr/bin/python
# coding=utf-8


from django.template import loader,Context
from django.http import HttpResponse
from gallery.models import Blog
from django.shortcuts import render
from django.db.models import Q

def Posts(request):
    context = {}
    context['posts'] = Blog.objects.all()
    archive_link = time_line(request)
    context.update(archive_link)
    return render(request,'posts.html',context)
    


def blog_detail(request,id=None):
    context = {}
    blog = Blog.objects.get(pk=id)
    context['blog'] = blog
#    context['id'] = id
    return render(request,'blog_detail.html',context)


def search(request):
    context = {}
    key = request.GET.get('search','')
    context['key'] = key
    context['blogs'] = Blog.objects.filter(title__icontains=key).order_by('-timestamp')
    return render(request,'search.html',context)

def time_line(request):
    context = {}
#    all_time_line = []
    blogs_list = []
#    blogs = Blog.objects.all()
    blogs= Blog.objects.values('id','title', 'timestamp').order_by('timestamp')
#    for blog in blogs:
#        if blog.timestamp not in all_time_line:
#            all_time_line.append(blog.timestamp)
#    context['all_time_line'] = all_time_line
    dates = set([str(i['timestamp'].year)+str(i['timestamp'].month) for i in blogs])
    for i in dates:
        dic = {}
        b_info = []
        count = 0
        dic['year'] = i[:4]
        dic['month'] = i[4:]
        for obj in blogs:
            if str(obj['timestamp'].year) + str(obj['timestamp'].month) == i:
                dic_ = {}
                dic_['blog'] = obj
                b_info.append(dic_)
                count += 1
        dic['count'] = count
        dic['b_info'] = b_info
        blogs_list.append(dic)
    
    context['dates'] = blogs_list
#    context['blogs'] = blogs
    return context
   # return render(request,'posts.html',context)
    
def archive(request):
    context = {}
    post = []
    year = request.GET.get('year','')
    month = request.GET.get('month','')
    blogs = Blog.objects.filter(Q(timestamp__month = month), Q(timestamp__year = year))
    context['posts'] = blogs
    archive_link = time_line(request)
    context.update(archive_link)
 
    return render(request,'posts.html',context)
