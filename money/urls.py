from django.urls import path, include
from rest_framework.routers import DefaultRouter
from money.views import TagViewSet, CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register('transaction', TransactionViewSet, 'transaction')
router.register('tag', TagViewSet, 'tag')
router.register('category', CategoryViewSet, 'category')

urlpatterns = [
    path('', include(router.urls))
]
