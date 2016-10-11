from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context, RequestContext
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from web.forms import registerForm
from web.models import UserInfo, FoodInfo, UserEvaluations, FoodRecommendations, RestaurantMenus, RestaurantInfo
from web.pyscript.Controller.RecommendationEngine import RecommendationEngine
from web.pyscript.Model.User import User
from web.pyscript.Model.RecommendationQueue import RecommendationQueue

# Create your views here.
def main_page(request):
    user = request.user
    #requestingUser = User(user.pk, user.username, user.password, user.age)
    #reQueue = RecommendationEngine().getFoodRecommendationQueue(requestingUser)

    #relistH = []
    #relistG = []
    #for item in range(1, 10):
    #    relistH.append(RecommendationEngine().runMapping(reQueue, '홍대'))
    #    relistG.append(RecommendationEngine().runMapping(reQueue, '강남'))

    #if request.is_ajax():
    #    if request.POST:
    #        count = int(request.POST['co'])
            
    #        if request.POST['loca'] == '강남':
    #            addContent = relistG[count]
    #        else:
    #            addContent = relistH[count]
            
    #        tpl = loader.get_template('webTemplates/index.html')
    #        ctx = Context({'relist': addContent})

    #        return HttpResponse(tpl.render(ctx))


    return render(request, 'webTemplates/index.html', {'user':user })


def ajax_form(request):
    rank = int(request.POST['rank'])

    try:
        foodID = FoodRecommendations.objects.get(recommendation=rank)
    except FoodRecommendations.DoesNotExist:
        return HttpResponse()
    print(foodID.foodID)
    print(type(foodID.pk))
    #foodInfo = FoodInfo.objects.get(id = foodID.pk)
    #print(foodInfo.name)
    foodInfo = FoodInfo.objects.raw('select * from web_foodinfo where id = %s', [foodID.pk])[0]
    print(foodInfo)
    
    '''
    for row in foodInfo:
        name = row['name']
        print(name)
    '''

    #resID = RestaurantMenus.objects.filter(foodId = foodID.pk)
    resID = RestaurantMenus.objects.raw('select * from web_restaurantmenus where foodId_id = %s', [foodID.pk])
    print(resID)

    resInfo = list()

    for item in resID:
            resInfo.append(RestaurantInfo.objects.get(id = item.restaurantId_id))

    value = RequestContext(request, {'item': foodInfo, 'res': resInfo})
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
    foodlist.append(FoodInfo.objects.get(id=21))
    foodlist.append(FoodInfo.objects.get(id=75))
    foodlist.append(FoodInfo.objects.get(id=83))
    foodlist.append(FoodInfo.objects.get(id=12))
    foodlist.append(FoodInfo.objects.get(id=40))
    foodlist.append(FoodInfo.objects.get(id=42))
    foodlist.append(FoodInfo.objects.get(id=39))
    foodlist.append(FoodInfo.objects.get(id=25))
    foodlist.append(FoodInfo.objects.get(id=44))
    foodlist.append(FoodInfo.objects.get(id=23))
    foodlist.append(FoodInfo.objects.get(id=59))
    foodlist.append(FoodInfo.objects.get(id=43))
    foodlist.append(FoodInfo.objects.get(id=2))
    foodlist.append(FoodInfo.objects.get(id=15))
    foodlist.append(FoodInfo.objects.get(id=16))
    foodlist.append(FoodInfo.objects.get(id=54))
    foodlist.append(FoodInfo.objects.get(id=85))
    foodlist.append(FoodInfo.objects.get(id=86))
    foodlist.append(FoodInfo.objects.get(id=61))
    foodlist.append(FoodInfo.objects.get(id=71))
    foodlist.append(FoodInfo.objects.get(id=98))
    foodlist.append(FoodInfo.objects.get(id=5))
    foodlist.append(FoodInfo.objects.get(id=6))
    foodlist.append(FoodInfo.objects.get(id=36))
    foodlist.append(FoodInfo.objects.get(id=20))
    foodlist.append(FoodInfo.objects.get(id=62))
    foodlist.append(FoodInfo.objects.get(id=38))
    foodlist.append(FoodInfo.objects.get(id=91))
    foodlist.append(FoodInfo.objects.get(id=82))
    foodlist.append(FoodInfo.objects.get(id=37))

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
