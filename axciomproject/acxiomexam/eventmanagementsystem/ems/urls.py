from django.urls import path
from.import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('admin_index',views.admin_index,name='admin_index'),
    path('maintain_user',views.maintain_user,name='maintain_user'),
    path('maintain_vendor',views.maintain_vendor,name='maintain_vendor'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('edit_vendor/<int:id>',views.edit_vendor,name='edit_vendor'),
    path('del_user/<int:id>',views.del_user,name='del_user'),
    path('del_vendor/<int:id>',views.del_vendor,name='del_vendor'),
    path('user_index',views.user_index,name='user_index'),
    path('vendorpage',views.vendorpage,name='vendorpage'),
    path('catering',views.catering,name='catering'),
    path('lighting',views.lighting,name='lighting'),
    path('decoration',views.decoration,name='decoration'),
    path('flourist',views.flourist,name='flourist'),
    path('user_login',views.user_login,name='user_login'),
    path('user_signup',views.user_signup,name='user_signup'),
]