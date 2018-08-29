from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import LoginForm
from .models import user_mstr
from util.PasswordUtil import Util

# Create your views here.
def index(request):
	return render(request,'index.html')

def NGEstimate(request):
	return render(request,'base.html')
	
def j_check(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['login_id'])
			formPassword=form.cleaned_data['login_pwd']
			login_password=user_mstr.objects.values_list('login_pwd').filter(login_id=form.cleaned_data['login_id'])
			for j in login_password:
				password = j[0]
				
			#password=login_password.login_pwd
			d=Util.matchHashedText(password,formPassword)
			if d:
				return HttpResponseRedirect('/NGEstimate')
			#print(password)
			else:
				messages.error(request,"Invalid user name or Password!")
				return render(request, 'index.html')
	else:
		form = LoginForm()
	messages.error(request,"Invalid Error!")
	return render(request, 'index.html')
	