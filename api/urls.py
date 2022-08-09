from django.urls import path
from .views import CompanyView

urlpatterns = [
    # path('', main)
    path('company', CompanyView.as_view())
]
