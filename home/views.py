from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")  
    #HttpResponse for render string, but you will render templates
    return render(request,'home.html')

def about(request):
    return HttpResponse("This is about page") 


def contact(request):
    return HttpResponse("This is contact page") 

def service(request):
    return HttpResponse("This is service page") 