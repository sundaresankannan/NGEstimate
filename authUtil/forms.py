from django import forms

class LoginForm(forms.Form):
	 
	login_id = forms.CharField(max_length=20)
	login_pwd = forms.CharField(max_length=120,widget=forms.PasswordInput)