from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator
import datetime

# Create your views here.


def Index(request):


        post_list = Post.objects.all().order_by('-created_at')
        paginator = Paginator(post_list, 3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'index.html', {'posts':posts})    
    
   
   


def Postist(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Post.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    tasksDone = Post.objects.filter(done='done', user=request.user).count()
    tasksDoing = Post.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = Post.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = Post.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = Post.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'post.html', 
        {'tasks':tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing })


def Services(request):
    
    return render(request, 'services.html')
    

def Elementos(request):
    
    return render(request, 'elementos.html')


def Contato(request):
    
    return render(request, 'contato.html')

def Sobre(request):
    
    return render(request, 'sobre.html')        
