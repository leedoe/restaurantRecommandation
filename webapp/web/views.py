from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from web.forms import registerForm
from web.models import UserInfo, Food, UserFoodPreference
from web.pyscript.Controller.RecommendationEngine import RecommendationEngine
from web.pyscript.Model.User import User
from web.pyscript.Model.RecommendationQueue import RecommendationQueue

# Create your views here.
def main_page(request):
    user = request.user
    requestingUser = User(user.pk, user.username, user.password, user.age)
    reQueue = RecommendationEngine().getFoodRecommendationQueue(requestingUser)

    relistH = []
    relistG = []
    for item in range(1, 10):
        relistH.append(RecommendationEngine().runMapping(reQueue, '홍대'))
        relistG.append(RecommendationEngine().runMapping(reQueue, '강남'))

    if request.is_ajax():
        if request.POST:
            count = int(request.POST['co'])
            
            if request.POST['loca'] == '강남':
                addContent = relistG[count]
            else:
                addContent = relistH[count]
            
            tpl = loader.get_template('webTemplates/recommend.html')
            ctx = Context({'relist': addContent})

            return HttpResponse(tpl.render(ctx))

    return render(request, 'webTemplates/main.html', {'user':user })


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

            return redirect('/prefer')

    elif request.method == "GET":
        userform = registerForm()

    return render(request, 'webTemplates/userRegisteration.html', {"userform": userform})


def prefer(request):
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


def wordCloud(request):
    user = request.user
    requestingUser = User(user.pk, user.username, user.password, user.age)
    reQueue = RecommendationEngine().getFoodRecommendationQueue(requestingUser)
    wordList = RecommendationEngine().getWordCloudList(reQueue, 20)
    
    return render(request, 'webTemplates/wordCloud.html', {'wordList': wordList})