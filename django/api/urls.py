from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import loginfunc, reserve_data


router = routers.DefaultRouter()

urlpatterns = [

    path('', include(router.urls)),
    path('login/', loginfunc, name='login'),
    path('reserve_data/', reserve_data, name='reserve'),
]
