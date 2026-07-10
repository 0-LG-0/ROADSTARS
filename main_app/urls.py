from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_index, name='post-index'),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post-create'),
    path('accounts/login/', views.Login.as_view(), name='user-login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/user/', views.user_index, name='user-post-index'),
    path('posts/user/<int:post_id>/', views.user_detail, name='user-post-detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('events/', views.event_index, name='event-index'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail'),
    path('events/user/', views.event_user_index, name='user-event-index'),
    path('events/user/<int:event_id>/', views.event_user_detail, name='user-event-detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('user/profile/', views.user_profile, name='user-profile'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
]