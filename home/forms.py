from django import forms  # to get data from form



class PersonalInfoForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    job = forms.CharField(max_length=100)
    job_location = forms.CharField(max_length=100)
    hometown = forms.CharField(max_length=100)