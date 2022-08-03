from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('form',views.get_name,name='form'),
    path('form/<slug:slug>/',views.edit,name='edit'),
]