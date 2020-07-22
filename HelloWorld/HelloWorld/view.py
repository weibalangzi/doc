from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)