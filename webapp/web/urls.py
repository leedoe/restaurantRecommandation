
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from web.forms import LoginForm

from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'webTemplates/loginPage.html', 'authentication_form': LoginForm}),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^registration/$',views.UserRegister, name="signup"),
    url(r'^prefer/$', views.prefer, name='perfer'),
    url(r'^main/$', views.main_page, name='main'),
]

