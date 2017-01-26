from login.models import UserProfile, Project
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email','password')
		labels = {
                          'first_name' :('First Name'),
                          'last_name' :('Last Name'),
                          'Username' :('Username'),
                          'email' :('E-mail ID'),
                          'password' :('Password'),
                        }

class UserProfileForm(forms.ModelForm):
    branch = forms.CharField(
        widget = formas.TextInput(attrs = {'class':"input-lg", 'size':"40"}),
    )
    domain = forms.CharFeild(
        widget = forms.TextInput(attrs = {'class':"input-lg", 'size':"40"}),
    )
    class Meta:
	    model = UserProfile
		fields = ('branch','domain')
		labels = {
                 'branch' :('Branch'),
                 'domain' :('Domain'),
                 }

class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
    )

    description = forms.CharField(
       widget=forms.Textarea(attrs={'rows':"5",'class': "input-lg",'cols':"40"}),
    )

    video_url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg",'size':"40"}),
    )

   

    class Meta: 
        model = Project
        fields = ('title', 'video_url', 'description')
        labels = {
                'title': ('Project Name'),
                'description':('Add a description'),
                'video_url': ('Add a video'),
                }
