from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from web.forms import registerForm
from web.models import UserInfo, Food, UserFoodPreference


# Create your views here.
def main_page(request):
    return render(request, 'webTemplates/main.html')


def UserRegister(request):
    if request.method == "POST":
        userform = registerForm(request.POST)
        if userform.is_valid():
            un = userform.cleaned_data['username']
            pw1 = userform.cleaned_data['password1']
            age = userform.cleaned_data['age']
            user = UserInfo.objects.create_user(username=un, password=pw1, age=age)
            user.save()

            authUser = authenticate(username=un, password=pw1)
            login(request, authUser)

            return redirect('/perfer')

    elif request.method == "GET":
        userform = registerForm()

    return render(request, 'webTemplates/userRegisteration.html', {"userform": userform})


def perfer(request):
    user = request.user

    if request.is_ajax():
        if request.POST:
            uid = user.pk
            fid = request.POST['foodid']
            score = request.POST['grade']
            
            foodInstance = Food.objects.get(id=fid)
            prefer, created = UserFoodPreference.objects.update_or_create(userID=user, foodID=foodInstance, defaults={'score': 0})
            prefer.score=int(score) + 1
            prefer.save()
            return HttpResponse('')
    
    fl = list()
    foodlist = Food.objects.all()

    for item in foodlist:
        try:
            fp = UserFoodPreference.objects.get(foodID = item, userID=user)
            score = fp.score
            num = 5-score
        except:
            fp = None
            score = 0
            num = 5
        #print(item)
        #print(fp)
        fl.append((item, fp, score, num))
    return render(request, 'webTemplates/perfer.html', {'foodlist': fl, 'user': user })

