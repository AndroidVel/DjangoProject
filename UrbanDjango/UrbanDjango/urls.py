"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import view_class, ViewFunc
from task3.views import Shop, Cart, MainPage


contex = {
    'game1': 'WarThunder',
    'game2': 'Squad',
    'game3': 'CALL of DUTY'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', view_class),
    path('func/', ViewFunc.as_view()),
    path('platform/', MainPage.as_view()),
    path('platform/games/', Shop.as_view(), contex),
    path('platform/cart/', Cart.as_view())
]
