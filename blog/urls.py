from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostViewSet

router = DefaultRouter()
router.register('articles', PostViewSet, 'post')
# router.register('article', PostViewSet, 'post')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api/', include(router.urls)),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]