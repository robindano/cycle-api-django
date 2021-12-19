from django.urls import path
from gifts import views

urlpatterns = [
    path('', views.GiftList.as_view()),
    path('<int:pk>/', views.GiftDetail.as_view())
]