from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostFunc.index, name="Index"),
    path('content/<str:slug>', views.PostFunc.content, name="content"),
    path('category/<str:Category>', views.PostFunc.category, name="category"),
    path('search/', views.PostFunc.search, name="search"),
    path('addContent/', views.PostFunc.addContent, name="addContent"),
    path('contact/', views.PostFunc.contact, name="contact"),
    path('vc/', views.PostFunc.validateContact, name="validateContact"),
    path('validate/', views.PostFunc.validate, name="validate"),
    path('signup/', views.utility.handleSignup, name="signup"),
    path('login/', views.utility.handleLogin, name="login"),
    path('logout/', views.utility.handleLogout, name="logout"),
    path('displayall/', views.PostFunc.DisplayAll, name="display"),
    path('userposts/', views.userUtility.userPost, name="user_post"),
    # Remove this
    path('test/', views.PostFunc.test, name="user_post"),
]