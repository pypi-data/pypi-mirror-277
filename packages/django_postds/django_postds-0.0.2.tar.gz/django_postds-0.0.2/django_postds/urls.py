from django.urls import path
from . import views


app_name = 'postds'


urlpatterns = [
    path('<slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
