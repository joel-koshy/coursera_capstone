from django.urls import path, include
from .views import  MenuItemsView, SingleMenuItemsView, BookingViewSet, home

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu/', MenuItemsView.as_view(), name='menu'), 
    path('menu/<int:pk>', SingleMenuItemsView.as_view()),
    path('home', home), 
    path('booking/', include(router.urls), name='book'), 

]