from django.shortcuts import render,HttpResponse,redirect
from to_do.models import list
# Create your views here.
def home(request):
    context ={'success': False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        chunk=list(listTitle=title,listDes=desc)
        chunk.save()
        context ={'success': True}
    return render(request,'index.html',context)

def todolist(request):
    alltask=list.objects.all()
    # for items in alltask:
    #     print(items.listDes)
    context={'tasks':alltask}
    return render(request, 'list.html',context)

def delete(request,name):
    list.objects.filter(listDes=name).delete()
    return redirect('todolist')

def profile(request):
    return render(request,"profile.html")