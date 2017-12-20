from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import models

class Theme(models.Model):
    theme_article = models.TextField()
    theme_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.theme_article

class Comment(models.Model):
    comment_content = models.TextField()
    comment_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    comment_likes = models.BigIntegerField()
    def __str__(self):
        return self.comment_content


