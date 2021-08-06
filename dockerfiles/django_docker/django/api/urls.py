from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViewSet, ManageUserView
from api.views import loginfunc, input_func, search_value, search_values_1year, upload_file, reserve_data, CreateUserView


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)  # 認証していればタスクが見れる
router.register('users', UserViewSet)

urlpatterns = [

    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
    path('login/', loginfunc, name='login'),
    path('input/', input_func, name='input_func'),
    path('output/', search_value, name='output_func'),
    path('outputs/', search_values_1year, name='output_func_many'),
    path('upload/', upload_file, name='upload_file'),
    path('reserve_data/', reserve_data, name='reserve'),
    path('register/', CreateUserView.as_view(), name='register'),
]
