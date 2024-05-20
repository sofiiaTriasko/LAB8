from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
