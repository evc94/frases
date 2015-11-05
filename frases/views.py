from django.shortcuts import render

def post_list(request):
    return render(request, 'frases/post_list.html', {})
