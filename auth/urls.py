from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from auth.views import RegisterView

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register')
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)