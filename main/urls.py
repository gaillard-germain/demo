from django.urls import path
from . import views

urlpatterns = [
    path('api/user_list', views.UserList.as_view()),
]
