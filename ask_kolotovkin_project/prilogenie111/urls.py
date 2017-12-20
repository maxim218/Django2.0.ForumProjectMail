from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.authorization, name='authorization'),
    url(r'^checkin/', views.checkin, name='checkin'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^authorizeusermethod/', views.authorizeusermethod, name='authorizeusermethod'),
    url(r'^getMyLogin/', views.getMyLogin, name='getMyLogin'),
    url(r'^outfromsite/', views.outfromsite, name='outfromsite'),
    url(r'^theme/', views.theme, name='theme'),
    url(r'^adding_theme/', views.adding_theme, name='adding_theme'),
    url(r'^discuss/', views.discuss, name='discuss'),
    url(r'^getThemeInfo/', views.getThemeInfo, name='getThemeInfo'),
    url(r'^adding_comment/', views.adding_comment, name='adding_comment'),
    url(r'^result_page/', views.result_page, name='result_page'),
    url(r'^get_comments_of_theme/', views.get_comments_of_theme, name='get_comments_of_theme'),
]

