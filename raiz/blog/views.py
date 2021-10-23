



from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.


def Animes(request):

    posts = Post.objects.filter(categorias__id=1) # id=1 (animes)
    
   

    return render(request, 'animes.html', {'posts':posts})  

def Tecnologia(request):

    posts = Post.objects.filter(categorias__id=2) # id=2 (Tecnologia)
            
    return render(request, 'tecnologias.html', {'posts':posts})   


#Metodo responsavel por fazer o VISUALIZAR os detalhes do Post

def post(request, post_id):

     post = Post.objects.get(pk=post_id) 
     
    
     return render(request, 'post.html', {'post':post})  

           


#Metodo responsavel por fazer o CREATE do Post
def NovoPost(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'novo_post.html', {'form': form})

#Metodo responsavel por fazer um UPDATE do Post
@login_required
def EditarPost(request, pk):
    
    buscar_item = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=buscar_item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'editar_post.html', {'form': form})
    

#Metodo responsavel por fazer o VISUALIZAR os detalhes do Post
#@login_required


     
#Metodo responsavel por fazer o DELETE do Produto
@login_required
def DeletarPost(request, pk):
    buscar_item = get_object_or_404(Post, pk=pk)
    #form = ProdutosForm(request.POST or None, request.FILES or None, instance=buscar_produtos)
    if request.method == 'POST':
        buscar_item.delete()
        return redirect('index')

    return render(request, 'deletar_post.html', {'deletar': buscar_item})


def post_detailview(request, id):
    
  if request.method == 'POST':
    cf = CommentForm(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      comment = Comment.objects.create(post = post, user = request.user, content = content)
      comment.save()
      return redirect(post.get_absolute_url())
    else:
      cf = CommentForm()
        
    context ={
      'comment_form':cf,
      }
    return render(request, 'post.html', context)    
