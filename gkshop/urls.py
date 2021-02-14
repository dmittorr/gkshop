"""gkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import mainapp.views as mainapp

<<<<<<< HEAD
urlpatterns =[
    path("admin/", admin.site.urls),
=======
urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> a8a45b5351b6bef9480f13403f1c60f33bf79939
    path("", mainapp.main),
    path("products/", mainapp.products),
    path("contact/", mainapp.contact),
]
