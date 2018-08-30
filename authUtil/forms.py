from django import forms
from .models import user_mstr

class LoginForm(forms.Form):
	 
	login_id = forms.CharField(max_length=20)
	login_pwd = forms.CharField(max_length=120,widget=forms.PasswordInput)

class UserMasterForm(forms.ModelForm):
    class Meta:
        model = user_mstr
        fields = ['login_id', 'login_pwd','last_name','first_name','startdate','enddate']
