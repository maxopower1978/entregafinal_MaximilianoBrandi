from django.shortcuts import render
from blog.models import Post  # Importamos el modelo de Post desde la app blog

def home(request):
    posts = Post.objects.all()  # Obtenemos todos los posts del blog
    return render(request, 'core/home.html', {'posts': posts})
