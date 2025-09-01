from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='api-index'),
    path('post/', views.index_post, name='api-index-post'),
    path('items/', views.get_all_item, name='api-get-all-items'),
    path('items/create/', views.create_item, name='api-create-item'),
    path('items/<int:pk>/', views.update_or_delete_item, name='api-update-or-delete-item'),
]