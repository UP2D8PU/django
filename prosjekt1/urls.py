"""prosjekt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.views.generic import TemplateView
#from loginn.views import register, register_success, logout_page, home
from core import views as core_views


urlpatterns = [
#    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^form/', include('form.urls')),
    url(r'^startHome/', include('startHome.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
               #url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
               #url(r'^logout/$', logout_page, name='logout'),
               #url(r'^accounts/login/$', auth_views.login, name='loginn'), # If user is not login it will redirect to login page
               #url(r'^register/$', register, name='register'),
               #url(r'^register/success/$', register_success, name='registersuccess'),
               #url(r'^home/$', home, name='home'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    
    
]
