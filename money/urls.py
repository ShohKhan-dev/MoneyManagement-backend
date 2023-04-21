from django.urls import path, include
from rest_framework.routers import DefaultRouter
from money.views import TagViewSet, TransactionViewSet

router = DefaultRouter()
router.register('transaction', TransactionViewSet, 'transaction')
router.register('tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(router.urls))
]
