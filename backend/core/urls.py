from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TotalAPIView
from .views import TokenTAPIList, TotalAPIView, TokenAPIView

# from .views import TokenTAPIList, TokenTAPICreate, TotalAPIView, TokenAPIView

# router = DefaultRouter()
# router.register(r'tokens', TotalAPIView)

urlpatterns = [
    path('list/', TokenTAPIList.as_view()),
    path('total_supply/', TotalAPIView.as_view()),
    path('createss/', TokenAPIView.as_view()),
    # path('create/', TokenTAPICreate.as_view()),
    # path("", include(router.urls)),

]
