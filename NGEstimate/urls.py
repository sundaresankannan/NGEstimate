"""NGEstimate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from authUtil.views import index,j_check,NGEstimate,UserMaster,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^index/', view=index),
	url(r'^$',view=index),
	url(r'^logout/',view=logout,name='User Logout'),
	#url(r'^login/',view=user_login,name='User Login'),
	url(r'^j_check/',view=j_check,name='Security Check'),
	url(r'^NGEstimate/',view=NGEstimate,name='EstimateScreen'),
	url(r'^UserMaster/',view=UserMaster,name='UserMaster'),
]
