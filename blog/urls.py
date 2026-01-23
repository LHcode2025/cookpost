from django.urls import path
from . import views


urlpatterns = [    
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.postCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.postUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.postDeleteView.as_view(), name='post-delete'),
]