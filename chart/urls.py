from django.urls import path
from .views import ApiView, HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('api/',ApiView,name='api')
]
