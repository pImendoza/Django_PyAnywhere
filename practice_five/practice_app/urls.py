from django.urls import path
from practice_app import views


# TEMPLATE URLS!
app_name = 'practice_app'

urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]