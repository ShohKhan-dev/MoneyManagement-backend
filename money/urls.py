from django.urls import path, include
from rest_framework.routers import DefaultRouter
from money.views import TagViewSet, TransactionViewSet, login_view, registration_view, LogoutView, UserView



router = DefaultRouter()
router.register('transaction', TransactionViewSet, 'transaction')
router.register('tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view()),
]
