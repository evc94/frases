from django.utils import timezone
from .models import Frase
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Frase.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'frases/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Frase, pk=pk)
    return render(request, 'frases/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('frases.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'frases/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Frase, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('frases.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'frases/post_edit.html', {'form': form})
