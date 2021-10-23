from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['title', 'summary', 'content', 'author', 'categorias', 'imagem']

        widgets = {
            'Titulo': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'Sumario': forms.Textarea(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'placeholder':'Conteúdo', 'class': 'form-control form-control-lg'}),
            'author': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'categorias': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'imagem': forms.FileInput(attrs={'id':'validatedCustomFile'}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = Comment
        fields =['content']        