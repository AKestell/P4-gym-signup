from . import views
from django.urls import path


urlpatterns = [
    path('', views.GymClassView.as_view(), name='home'),
]