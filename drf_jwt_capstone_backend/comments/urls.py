from django.urls import path
from comments import views

urlpatterns = [
    path('<int:gift_id>/', views.CommentList.as_view()),
    path('<int:gift_id>/<int:pk>/', views.CommentDetail.as_view())
]