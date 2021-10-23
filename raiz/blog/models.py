
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from users.models import User
from django.db import models


  
 

# Create your models here.


class Categoria(models.Model):

    title = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    

    def __str__(self) :
        return self.title


class Post(models.Model):

    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    categorias = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='blog/', blank=True)

    class Meta:
        ordering = ('-created_at', )

    
    def __str__(self) :
        return self.title



class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  content = models.TextField()

        

