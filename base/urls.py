from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('test2/', views.test2),
	path('test3/', views.test3),
	path('test4/', views.test4),

]
