from django.shortcuts import render
from django.utils import timezone
from .models import Frase

def post_list(request):
    posts = Frase.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'frases/post_list.html', {'posts': posts})
