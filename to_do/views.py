from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def list(request):
    return render(request, 'list.html')