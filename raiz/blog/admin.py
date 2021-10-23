from django.contrib import admin

# Register your models here.

from blog.models import Post, Categoria, Comment


admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comment)

