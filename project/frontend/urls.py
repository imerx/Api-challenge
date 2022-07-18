from django.urls import path

from . import views

urlpatterns = [
    path('random_crawl/<str:pk>/', views.crawl , name='random_crawl'),
    path('random_crawl_reverse/<str:pk>/', views.crawl_reverse , name='random_crawl_reverse'),
]