from django.urls import path, re_path
from .views import ApiView, HomeView
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

handler404 = 'chart.views.page_not_found'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('api/<str:interval>',ApiView,name='api'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
