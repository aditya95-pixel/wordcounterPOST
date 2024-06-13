from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def counter(request):
    text=request.POST['text']
    l=text.split(" ")
    num=len(l)
    return render(request,"counter.html",{"num":num})
# Create your views here.
