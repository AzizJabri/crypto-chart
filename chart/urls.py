from django.urls import path
from .views import ApiView, HomeView
from django.conf.urls import handler404

handler404 = 'chart.views.page_not_found'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('api/<str:interval>',ApiView,name='api')
]
