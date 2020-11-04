from django.urls import path
from . import views

urlpatterns = [
    path('', views.GamePostListView.as_view(), name="game"),
    path('<int:pk>/', views.GamePostDetailView.as_view(), name="game-post-detail"),
    path('new/', views.GamePostCreateView.as_view(), name="game-post-create"),
    path('<int:pk>/update/', views.GamePostUpdateView.as_view(), name="game-post-update"),
    path('<int:pk>/delete/', views.GamePostDeleteView.as_view(), name="game-post-delete"),
]
