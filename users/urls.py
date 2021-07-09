from django.urls import path
from users import views
urlpatterns = [
    path('', views.index, name='index'), # landing page 
    path('dashboard/',views.dashboard, name='dashboard'), # auth'd user dashboard
]