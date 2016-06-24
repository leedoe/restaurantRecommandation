from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def main_page(request):
    output="<html><head><title></title></head><body><h1>TEST</h1></body></html>"
    return HttpResponse(output)


def UserRegister(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                reverse('signup_ok')
            )
    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, 'webTemplates/userRegisteration.html', {"userform": userform})
