from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'watchlist'

urlpatterns = [
    path('movies/', views.WatchListApiView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.WatchListDetailApiView.as_view(), name='movie_detail'),
    path('streams/', views.StreamPlatformListApiView.as_view(), name='stream_list'),
    path('streams/<int:pk>', views.StreamPlatformDetailApiView.as_view(), name='stream_detail'),
    path('movies/<int:movie_id>/reviews/', views.ReviewListGeneral.as_view(), name='review_list'),
    path('movies/<int:movie_id>/reviews/create', views.ReviewCreate.as_view(), name='review_create'),
    path('movies/reviews/<int:pk>', views.ReviewDetailGeneral.as_view(), name='review_detail'),
    path('users/reviews/', views.UserReviews.as_view(), name='user-reviews'),
]
