from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.req),
    path('admin/', admin.site.urls),
    path('home/', views.req),
    path('tq/', views.req),
    path('graph/', views.req),
]
