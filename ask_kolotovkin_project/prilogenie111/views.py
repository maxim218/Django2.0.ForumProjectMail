from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.db import models
from .models import Theme
from .models import Comment


def normalChar(c):
    alf = "abcdefghijklmnopqrstuvwxyz_0123456789"
    n = len(alf)
    for i in range(0,n):
        if c == alf[i]:
            return True
    return False

def normalString(s):
    n = len(s)
    if n == 0:
        return False
    for i in range(0,n):
        c = s[i]
        if normalChar(c) == False:
            return False
    return True

def getThemeInfo(request):
    pk = int(request.GET['a'])
    my_records_arr = Theme.objects.filter(pk=pk)
    record = my_records_arr[0]
    answer = str(record.theme_user) + "@@@@@_____~~~~~~" + str(record.theme_article)
    return HttpResponse(str(answer))

def discuss(request):
    return render(request, 'prilogenie111/discuss.html', {})

def result_page(request):
    return render(request, 'prilogenie111/result_page.html', {})

def theme(request):
    my_records_arr = Theme.objects.order_by('pk')
    my_records_arr = my_records_arr.reverse()
    return render(request, 'prilogenie111/theme.html', {'my_records_arr':my_records_arr})

def authorization(request):
    return render(request, 'prilogenie111/authorization.html', {})

def checkin(request):
    return render(request, 'prilogenie111/checkin.html', {})

def registration(request):
    user_login = str(request.POST['a'])
    user_password = str(request.POST['b'])

    if(normalString(user_login) == False):
        return HttpResponseRedirect("/checkin/" + "?x=no_correct_input")
    if (normalString(user_password) == False):
        return HttpResponseRedirect("/checkin/" + "?x=no_correct_input")

    # try to find user in db
    users = User.objects.filter(username=user_login)
    if len(users) > 0:
        # user is already exists in DB
        return HttpResponseRedirect("/checkin/" + "?x=registration_in_system_no")
    else:
        # registrate new user
        user = User.objects.create_user(user_login, user_login + "@abc.ru", user_password)
        user.save()
        return HttpResponseRedirect("/checkin/" + "?x=registration_in_system_yes")


def authorizeusermethod(request):
    user_login = str(request.POST['a'])
    user_password = str(request.POST['b'])

    if (normalString(user_login) == False):
        return HttpResponseRedirect("/" + "?x=no_correct_input")
    if (normalString(user_password) == False):
        return HttpResponseRedirect("/" + "?x=no_correct_input")

    # try to get user in Db
    user = authenticate(username=user_login, password=user_password)

    # if user exists
    if user is not None:
        # authorize user
        login(request, user)
        return HttpResponseRedirect("/" + "?x=authorize_of_user_yes")
    else:
        # error of authoring
        return HttpResponseRedirect("/" + "?x=authorize_of_user_yes_no")

def getMyLogin(request):
    if request.user.is_authenticated:
        user_login = str(request.user.username)
        return HttpResponse(str(user_login))
    else:
        return HttpResponse(str("Гость"))

def outfromsite(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/" + "?x=logout_from_site")

def adding_theme(request):
    if request.user.is_authenticated:
        theme_article = str(request.POST['a'])
        if len(theme_article) == 0:
            return HttpResponseRedirect("/theme/" + "?x=input_field_is_empty")
        else:
            Theme.objects.create(theme_article=theme_article, theme_user=request.user)
            return HttpResponseRedirect("/theme/" + "?x=add_theme_complete")
    else:
        return HttpResponseRedirect("/theme/" + "?x=user_is_not_autentificated_in_system")


def adding_comment(request):
    theme_number = int(request.POST['b'])
    comment_theme_array = Theme.objects.filter(pk=theme_number)
    comment_theme = comment_theme_array[0]

    if request.user.is_authenticated:
        comment_content = str(request.POST['a'])
        if len(comment_content) == 0:
            return HttpResponseRedirect("/result_page/" + "?x=input_field_is_empty")
        else:
            Comment.objects.create(comment_content=comment_content, comment_user=request.user, comment_theme=comment_theme, comment_likes=0)
            return HttpResponseRedirect("/result_page/" + "?x=push_comment_ok")
    else:
        return HttpResponseRedirect("/result_page/" + "?x=user_is_not_autentificated_in_system")


def get_comments_of_theme(request):
    theme_number = int(request.GET['b'])
    theme_array = Theme.objects.filter(pk=theme_number)
    theme = theme_array[0]

    comments_array = Comment.objects.filter(comment_theme=theme).order_by('pk')
    comments_array = comments_array.reverse()
    answer = ""
    for record in comments_array:
        s = str(record.comment_user) + "@@@@@_____~~~~~~" + str(record.comment_content)
        answer = answer + s + "@@@@@@@@@@@@@@@@@@_________________~~~~~~~~~~~~~~~~"
    return HttpResponse(str(answer))

