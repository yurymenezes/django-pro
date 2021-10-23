from django.urls import path, include
from .views import Index, Services, Elementos, Contato, Sobre

urlpatterns = [

    path('', Index, name='index'),
    path('services/', Services, name='services'),
    path('elementos/', Elementos, name='elementos'),
    path('contato/', Contato, name='contato'),
    path('sobre/', Sobre, name='sobre')


   
]
