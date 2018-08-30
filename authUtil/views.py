from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import LoginForm,UserMasterForm
from .models import user_mstr
from util.PasswordUtil import Util
from functools import wraps
# Create your views here.
login_id,login_user = '',''

"""
required_login is the decorator function which help to use the URL that session required, if empty that need to redirect to index

"""
def required_login(view_func):
	@wraps(view_func)
	def wrapper(request, *args, **kwargs):
		print(login_id)
		try:
			if request.session['username'] == login_id:
				return view_func(request,*args,**kwargs)
			else:
				return render(request, 'index.html')
		except KeyError:
			return render(request, 'index.html')
		
	return wrapper


def index(request):
	try:
		if request.session['username'] == login_id:
			return HttpResponseRedirect('/NGEstimate')
		else:
			return render(request, 'index.html')
	except KeyError:
		return render(request, 'index.html')

def logout(request):
	try:
		del request.session['username']
	except KeyError:
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')
	
@required_login
def NGEstimate(request):	
	global login_user 
	context = {'user_name':login_user}
	return render(request,'base.html',context=context)

@required_login
def UserMaster(request):
	global login_user 
	context = {'user_name':login_user}
	form = UserMasterForm(request.POST)
	return render(request,'UserMaster.html',{'form':form})
	
def j_check(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		password=''
		if form.is_valid():
			global login_id,login_user
			formPassword=form.cleaned_data['login_pwd']
			login_password=user_mstr.objects.values_list('login_pwd').filter(login_id=form.cleaned_data['login_id'])
			user_name = user_mstr.objects.values_list('last_name','first_name').filter(login_id=form.cleaned_data['login_id'])
			login_id = form.cleaned_data['login_id']
			request.session['username'] = login_id
			request.session.set_expiry(900)
			print(request.session['username'])
			for j in login_password:
				password = j[0]
			for i in user_name:
				login_user = i[0] + " "+i[1]
			#login_user=(user_name[0]+" "+user_name[1])
			print(login_user)
			#password=login_password.login_pwd
			d=Util.matchHashedText(password,formPassword)
			if d:
				return HttpResponseRedirect('/NGEstimate')
			
			else:
				messages.error(request,"Invalid user name or Password!")
				return render(request, 'index.html')
	else:
		form = LoginForm()
	#messages.error(request,"Invalid Error!")
	return render(request, 'index.html')


