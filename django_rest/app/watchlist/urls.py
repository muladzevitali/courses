from django.urls import path
from . import views

app_name = 'watchlist'
urlpatterns = [
    path('movies/', views.WatchListApiView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.WatchListDetailApiView.as_view(), name='movie_detail'),
    path('streams/', views.StreamPlatformListApiView.as_view(), name='stream_list'),
    path('streams/<int:pk>', views.StreamPlatformDetailApiView.as_view(), name='stream_detail'),
]
