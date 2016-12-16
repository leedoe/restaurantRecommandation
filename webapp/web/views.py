from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context, RequestContext
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db import connection

from web.forms import registerForm
from web.models import UserInfo, FoodInfo, UserEvaluations, FoodRecommendations, RestaurantMenus, RestaurantInfo
from web.pyscript.Controller.RecommendationEngine import RecommendationEngine
from web.pyscript.Model.User import User
from web.pyscript.Model.RecommendationQueue import RecommendationQueue

import urllib.request
from urllib.parse import quote
import json

# Create your views here.
def main_page(request):
    user = request.user
    clusterId = user.cluster_id

    return render(request, 'webTemplates/index.html', {'user':user, 'clusterId': user.cluster_id})


def ajax_form(request):
    rank = int(request.POST['rank'])
    clusterId = int(request.POST['clusterID'])

    try:
        foodID = FoodRecommendations.objects.get(recommendation=rank)
    except FoodRecommendations.DoesNotExist:
        return HttpResponse()
    
    foodInfo = FoodInfo.objects.get(id = foodID.pk)
    
    #expectedScore
    avgScore = None
    with connection.cursor() as cursor:
        cursor.execute(
                'select avg(usereval.score) as id ' +
                'from django.web_userevaluations usereval ' +
                'inner join django.web_userinfo userinfo on usereval.userID_id = userinfo.id ' +
                'where userinfo.cluster_id_id = ' + str(clusterId) +
                ' and usereval.foodID_id = ' +str(foodID.pk))
        avgScore = cursor.fetchone()

    resID = RestaurantMenus.objects.filter(foodId = foodID.pk)

    resInfo = list()
    mapcode = list()

    #geocoder
    client_id = 'roCnpNLInf37Lz76VwbT'
    client_secret = 'w0OdkWpu9p'
    

    for item in resID:
            temp = RestaurantInfo.objects.get(id = item.restaurantId_id)
            resInfo.append(temp)

            url = 'https://openapi.naver.com/v1/map/geocode?query=' + quote(temp.address)

            requestGeo = urllib.request.Request(url)

            requestGeo.add_header("X-Naver-Client-Id", client_id)
            requestGeo.add_header("X-Naver-Client-Secret", client_secret)

            response = urllib.request.urlopen(requestGeo)
            response_body = response.read().decode('UTF-8')

            content = json.loads(response_body)

            mapcode.append(content['result']['items'][0]['point'])

    

    print(mapcode)


    value = RequestContext(request, {'item': foodInfo, 'res': resInfo, 'avg': avgScore[0], 'mapcode': mapcode})
    template = loader.get_template('webTemplates/ajax_form.html')
    output = template.render(value)
    return HttpResponse(output)


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

    return render(request, 'webTemplates/regi.html', {"userform": userform})


def prefer(request):
    user = request.user

    if request.is_ajax():
        if request.POST:
            uid = user.pk
            fid = request.POST['foodid']
            score = request.POST['grade']
            
            foodInstance = FoodInfo.objects.get(id=fid)
            prefer, created = UserEvaluations.objects.update_or_create(userID=user, foodID=foodInstance, defaults={'score': 0})
            prefer.score=int(score) + 1
            prefer.save()
            return HttpResponse('')
    
    fl = list()
    #foodlist = FoodInfo.objects.all()

    foodlist = list();
    foodlist.append(FoodInfo.objects.get(id=20))
    foodlist.append(FoodInfo.objects.get(id=72))
    foodlist.append(FoodInfo.objects.get(id=80))
    foodlist.append(FoodInfo.objects.get(id=12))
    foodlist.append(FoodInfo.objects.get(id=38))
    foodlist.append(FoodInfo.objects.get(id=40))
    foodlist.append(FoodInfo.objects.get(id=37))
    foodlist.append(FoodInfo.objects.get(id=24))
    foodlist.append(FoodInfo.objects.get(id=42))
    foodlist.append(FoodInfo.objects.get(id=22))
    foodlist.append(FoodInfo.objects.get(id=57))
    foodlist.append(FoodInfo.objects.get(id=41))
    foodlist.append(FoodInfo.objects.get(id=2))
    foodlist.append(FoodInfo.objects.get(id=15))
    foodlist.append(FoodInfo.objects.get(id=16))
    foodlist.append(FoodInfo.objects.get(id=52))
    foodlist.append(FoodInfo.objects.get(id=82))
    foodlist.append(FoodInfo.objects.get(id=83))
    foodlist.append(FoodInfo.objects.get(id=59))
    foodlist.append(FoodInfo.objects.get(id=68))
    foodlist.append(FoodInfo.objects.get(id=95))
    foodlist.append(FoodInfo.objects.get(id=5))
    foodlist.append(FoodInfo.objects.get(id=6))
    foodlist.append(FoodInfo.objects.get(id=34))
    foodlist.append(FoodInfo.objects.get(id=19))
    foodlist.append(FoodInfo.objects.get(id=60))
    foodlist.append(FoodInfo.objects.get(id=36))
    foodlist.append(FoodInfo.objects.get(id=88))
    foodlist.append(FoodInfo.objects.get(id=79))
    foodlist.append(FoodInfo.objects.get(id=35))

    for item in foodlist:
        try:
            fp = UserEvaluations.objects.get(foodID = item, userID=user)
            score = fp.score
            num = 5-score
        except:
            fp = None
            score = 0
            num = 5
        #print(item)
        #print(fp)
        fl.append((item, fp, score, num))
    return render(request, 'webTemplates/prefer_b.html', {'foodlist': fl, 'user': user })


def wordCloud(request):
    user = request.user
    requestingUser = User(user.pk, user.username, user.password, user.age)
    reQueue = RecommendationEngine().getFoodRecommendationQueue(requestingUser)
    wordList = RecommendationEngine().getWordCloudList(reQueue, 20)
    
    return render(request, 'webTemplates/wordCloud.html', {'wordList': wordList})
