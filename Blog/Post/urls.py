from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('content/<str:slug>', views.content, name="content"),
    path('category/<str:Category>', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('addContent/', views.addContent, name="addContent"),
    path('contact/', views.contact, name="contact"),
    path('vc/', views.validateContact, name="validateContact"),
    path('validate/', views.validate, name="validate"),
    path('signup/', views.handleSignup, name="signup"),
    path('login/', views.handleLogin, name="login"),
    path('logout/', views.handleLogout, name="logout"),
    path('displayall/', views.DisplayAll, name="display"),
    path('userposts/', views.userPost, name="user_post"),
]