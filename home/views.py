from django.shortcuts import render,HttpResponse  # to render the output
from django.views.decorators.csrf import csrf_exempt  #to get the data from form
from .forms import PersonalInfoForm  # import from current pwd
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

def varRender(request):
    context = {
        'name':"Ranjit Singh",
        'job':"Machine Learning Engineer",
        'expertise':['python','data science','machine learning','NLP']
    }
    return render(request,'var_render.html',context)

def formsubmit(request):
    return render(request,'form_submit.html')
    # return HttpResponse('form page')



@csrf_exempt
def input_submit(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            job = form.cleaned_data['job']
            job_location = form.cleaned_data['job_location']
            hometown = form.cleaned_data['hometown']

            context = {
                'first_name':first_name,
                'last_name':last_name,
                'job':job,
                'job_location':job_location,
                'home_town':hometown
            }
            print(context)
            return render(request, 'form_data.html', {'first_name': first_name})  # Render a page with data
    else:
        form = PersonalInfoForm()
    return render(request, 'form_submit.html', {'form': form})
