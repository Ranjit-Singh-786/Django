from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render 

# to return string on a browser on "/" route 
# def home(request):
#     return HttpResponse("<h1>This is home page</h1>")

# to return the html templates 
def home(request):
    return render(request,'home.html')


def about(request):
    print(request.method) # has all the information regarding request
    return render(request,'about.html')

## To get the data 
blog_data = [{
    'first_name':'Ranjit Singh',
    'last_name':'last_name',
    'job':'job',
    'job_location':'job_location',
    'home_town':'home_town'
}]
def createblog(request):
    if request.method == 'GET':
        return render(request,'createblog.html')
    elif request.method == 'POST':
        data = request.POST  # all content in one time  
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        job = request.POST.get('job')
        job_location = request.POST.get('job_location')
        hometown = request.POST.get('hometown')
        print(data)
        sample_blog = dict()
        sample_blog['first_name'] = first_name
        sample_blog['last_name'] = last_name
        sample_blog['job'] = job 
        sample_blog['job_location'] = job_location
        sample_blog['hometown'] = hometown
        blog_data.append(sample_blog)  # we are keeping our data inside another variable 
        # to return normally data to the webpage 
        # return HttpResponse(f"<h1>{first_name} and {last_name}</h1>")
        return HttpResponseRedirect('/blogs')   # function to redirect to the another route 


def allblogs(request):
    # we are sending data to the another webpage 
    # data we have recieved from the form in createblog function 
    return render(request,'allblogs.html',{'data':blog_data})