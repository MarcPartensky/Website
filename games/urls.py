from django.urls import path
from . import views

urlpatterns = [
    path('', views.GamePostListView.as_view(), name="games"),
    path('game-post/<int:pk>/', views.GamePostDetailView.as_view(), name="game-post-detail"),
]