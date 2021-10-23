from django.urls import path, include
from .views import   Animes, NovoPost,  Tecnologia, NovoPost, EditarPost,  DeletarPost

urlpatterns = [

    
    
    path('animes/', Animes, name='animes'),
    path('tecnologia/', Tecnologia, name='tecnologia'),

    path('novo-post/', NovoPost, name='addpost'),
    path('editar-post/<int:pk>', EditarPost, name='updatepost'),

    path('deletar-post/<int:pk>', DeletarPost, name='deletepost'),
    

    
   
]
