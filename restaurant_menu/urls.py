from django.urls import path
from . import views

urlpatterns = [
    path('',views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(),name='menu_item')
]


# pycharm manage.py runserver   --- on termianl
# username: sanju   password:sanju
# email:sanjanaarj2003@gmail.com
#http://127.0.0.1:8000/admin    ---- in webpage(edge)