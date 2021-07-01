import re
from django.shortcuts import render,redirect,HttpResponseRedirect

from .models import magazine,checkavl,comment
from django.contrib import messages,auth
from django.shortcuts import get_object_or_404,Http404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .forms import *
from django.utils.text import slugify 
@login_required(login_url='login')
def details(request,id):
    k=0
    post=get_object_or_404(magazine,pk=id)
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        is_liked=True
    comments=comment.objects.filter(post=post).order_by('-id')
    if request.method=="POST":
        
        comment_form=commentform(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            c=comment.objects.create(post=post,user=request.user,content=content)
            k=1
            c.save()
            return HttpResponseRedirect(request.path_info)
            
        else:
            comment_form=commentform()

    if k==1:
        data={
        'card':post,
        'comments':comments,
        'comment_form':comment_form,
        'is_liked':is_liked,
        'total_likes':post.li(),
                }
    else:
        data={
        'card':post,
        'comments':comments,
        
                }

    return render(request, 'webpages/details.html',data)
    return render(request,'webpages/details.html')
def like_post(request):
    c=0
    post=get_object_or_404(magazine,id=request.POST.get('post_id'))
    p=post.id
    
    if 1:
        print(p)
        is_liked=False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked=False
        else:
            post.likes.add(request.user)
            is_liked=True
        
        if is_liked:
            print("hello world")
        else:
            print("sorry")
        

    k=0
    
    comments=comment.objects.filter(post=post).order_by('-id')



    data={
        'card':post,
        'comments':comments,
        'is_liked':is_liked,
        'total_likes':post.li(),
                }


    return render(request, 'webpages/details.html',data)

    




def result1(request):
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            d=checkavl.objects.filter(date__contains=keyword)
            if len(list(d))==0:
                return render(request,'webpages/result.html',{'data':None})
            else:
                return render(request,'webpages/result.html',{'data':d})



@login_required(login_url='login')
def search(request):      
    return render(request,'webpages/search.html')
def home(request):
    mag=magazine.objects.order_by('-createddate')

    data={
        'magz':mag,
        
    }
    
 
    return render(request,'webpages/home.html',data)
def about(request):
    return render(request,'webpages/about.html')
@login_required(login_url='login')
def check(request):
    if request.method=='POST':
        photo=request.FILES['photo']
        fullname=request.POST['name1']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        branch=request.POST['branch']
        subject=request.POST['subject']
        need=request.POST['need']
        details=request.POST['details']
        date=request.POST['date']
        
        k=checkavl(fullname=fullname,phonenumber=phonenumber,email=email,branch=branch,subject=subject,details=details,need=need,date=date,photo=photo)
        k.save()
        subject=fullname
        message=branch
        send_mail(
            subject,
            message, 
            'phanivedula76@gmail.com',
            ['pramodhsupreme@gmail.com'],
            fail_silently=False

        )
        messages.success(request,'message sent')
        return redirect('dashboard')
    return render(request,'check/index.html')
@login_required(login_url='login')
def dashboard(request):

    s=checkavl.objects.all()
    data={
        'p':s,
    }
    return render(request,'check/dashboard.html',data)
