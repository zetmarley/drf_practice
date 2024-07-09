from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MilageCreateAPIView, MilageListAPIView, MilageRetrieveAPIView, MilageUpdateAPIView, \
    MilageDestroyAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    # CRUD Moto
    path('moto/create', MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/<int:pk>', MotoRetrieveAPIView.as_view(), name='moto-info'),
    path('moto/update/<int:pk>', MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>', MotoDestroyAPIView.as_view(), name='moto-delete'),

    # CRUD milage
    path('milage/create', MilageCreateAPIView.as_view(), name='milage-create'),
    path('milage/', MilageListAPIView.as_view(), name='milage-list'),
    path('milage/<int:pk>', MilageRetrieveAPIView.as_view(), name='milage-info'),
    path('milage/update/<int:pk>', MilageUpdateAPIView.as_view(), name='milage-update'),
    path('milage/delete/<int:pk>', MilageDestroyAPIView.as_view(), name='milage-delete'),
] + router.urls