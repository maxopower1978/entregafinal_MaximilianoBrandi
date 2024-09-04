from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    posts = Post.objects.all()  # Obtener todos los posts
    return render(request, 'blog/home.html', {'posts': posts})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user.username  # Usamos el nombre de usuario del admin
        Post.objects.create(title=title, content=content, author=author)
        return redirect('home')
    return render(request, 'blog/create_post.html')

@login_required
@user_passes_test(is_admin)
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('home')
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
@user_passes_test(is_admin)
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})
