from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.UserApiView.as_view(), name="UserApiView"),
    path('list/', views.UserApiView.listUser, name='listUser'),
    path('delete/<int:id>', views.UserApiView.deleteUser, name='deleteUser'),
    path('post/', views.UserApiView.createUser, name='createUser'),
    path('post/<int:id>', views.UserApiView.createUser, name='updateUser'),

]
