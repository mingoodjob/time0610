from importlib.resources import path
from django.urls import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('new_order/<int:id>/', views.new_order, name='new_order'),
]
