from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='career'),
    path('login',views.login_views,name='login'),
    path('User',views.User_views,name='User'),
    path('AdminPanel',views.admin_views,name='AdminPanel'),
    path('logout',views.logout_views,name='logout'),
    path('approved/<int:pk>',views.feedback_approval,name='approved'),
    path('delete/<int:pk>',views.feedback_delete,name='delete'),

]    