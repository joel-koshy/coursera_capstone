from django.urls import path, include
from .views import  MenuItemsView, SingleMenuItemsView, BookingViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu/', MenuItemsView.as_view()), 
    path('menu/<int:pk>', SingleMenuItemsView.as_view()),

    path('booking/', include(router.urls)), 

]