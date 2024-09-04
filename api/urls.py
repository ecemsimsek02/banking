from django.urls import re_path as url , include
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView,
    CreateAccountAPIView,
    AccountListAPIView,
    ClientListCreateAPIView,
    WithdrawViewSet,
    DepositViewSet,
    #AccountBalanceViewSet,
    ClientViewSet,
    LogView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Bank App",
        default_version='v1',
        description="Bank App with Django Rest API",
        #terms_of_service="https://www.example.com/terms/",
        #contact=openapi.Contact(email="contact@example.com"),
        #license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'clients', ClientViewSet)


urlpatterns = [
    url(r'^branches/', BranchesAPIView.as_view(),name='branches'),
    url(r'^branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(),name='branch-detail'),
    url(r'^banks', BanksAPIView.as_view(), name='banks'),
    url(r'^bank/(?P<pk>[0-9]+)/', BankDetailAPIView.as_view(), name='bank-detail'),
    url(r'^create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    url(r'^accounts/', AccountListAPIView.as_view(), name='accounts'),
    url(r'^client/', ClientListCreateAPIView.as_view(),name='client'),
    url(r'^withdraws/', WithdrawViewSet.as_view(), name='withdraw-list'),
    url(r'^deposits/', DepositViewSet.as_view(), name='deposit-list'),
    #url(r'^account-balance/', AccountBalanceViewSet.as_view(),name='account-balance-list'),
    url(r'^log-view/', LogView.as_view(),name='log_view'),
    path('',include(router.urls)),
    path('log-view/', LogView.as_view(), name='log_view'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

