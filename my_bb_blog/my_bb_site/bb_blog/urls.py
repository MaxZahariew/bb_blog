from django.urls import path
from bb_blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int: id>/', views.post_detail, name='post_detail'),
]
