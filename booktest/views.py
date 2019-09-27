from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    # show book imformation
    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    # create a new book
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    b.save()
    # return HttpResponse('ok')
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request,bid):
    b = BookInfo.objects.get(id=bid)
    b.delete()
    return redirect('/index')


def areas(request):
    cur_area = AreaInfo.objects.get(atitle='广州市')
    p_area = cur_area.aParent
    next_area = cur_area.areainfo_set.all()
    return render(request, 'booktest/areas.html', {'cur_area':cur_area, 'p_area':p_area, 'next_area':next_area})
