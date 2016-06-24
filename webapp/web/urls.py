
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from web.forms import LoginForm


urlpatterns = [
    url(r'^$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'webTemplates/loginPage.html', 'authentication_form': LoginForm}),
    url(r'^registration/$',views.UserRegister, name="signup"),
    url(r'^perfer/$', template_name='webTemplates/perfer.html', name='perfer'),
]

