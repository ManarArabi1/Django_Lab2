"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lab1 import views

from Lab1.views import create, delete_student, home, about, contact, signin, signup, student, update
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home" ),
    path("contact/", contact, name="contact" ),
    path("about/", about, name="about" ),
    path("student/", student, name="student" ),
    path('delete_student/<int:id>',delete_student,name="delete_student"),
    path('signup/',signup,name="signup"),
    path('login/',signin,name="login"),
    path('create/',create,name="create"),
    path('update/<int:id>',update,name="update"),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),


]
