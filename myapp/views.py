from django.shortcuts import render

def child(request):
    return render(request,'child.html')

def base(request):
    return render(request,'base.html')


# Create your views here.
