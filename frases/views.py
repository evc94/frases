from django.shortcuts import render
from django.utils import timezone
from .models import Frase
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Frase.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'frases/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Frase, pk=pk)
    return render(request, 'frases/post_detail.html', {'post': post})
