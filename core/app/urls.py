from django.urls import path
from .views import UserRetrieveUpdateDestroy, UserListCreate, CatRetrieveUpdateDestroy, CatListCreate

urlpatterns = [
    path('users', UserListCreate.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDestroy.as_view()),
    path('cats', CatListCreate.as_view()),
    path('cats/<int:pk>', CatRetrieveUpdateDestroy.as_view()),
]
