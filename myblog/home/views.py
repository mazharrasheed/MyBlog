from django.shortcuts import redirect, render

# Create your views here.

def index(request):

  data={}
  return render(request,'index.html',data)

