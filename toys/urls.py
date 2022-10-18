from toys import views
from django.urls import path

urlpatterns = [
    path('toys/', views.toy_list),
    path('toys/<int:pk>', views.toy_detail),
]