from django.urls import path
from . import views

urlpatterns = [
    path('', views.films),
    # path('films', views.films),
]