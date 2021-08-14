from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViewSet, ManageUserView
from api.views import loginfunc, input_func, search_value, search_values_1year, upload_file,CreateUserView,name_to_code,predict_reg,predict_display


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
    path('register/', CreateUserView.as_view(), name='register'),
    path('serach_code/', name_to_code, name='serach_code'),
    path('predict_reg/', predict_reg, name='predict_reg'),
    path('predict_display/', predict_display, name='predict_display')
]
