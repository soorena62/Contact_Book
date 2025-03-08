from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import include, path
from .views import ContactListView, ContactDetailView, UserDetailView, UserListCreateView, LoginView
# Create Your URLS Here:


urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
]
