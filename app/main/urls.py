from django.urls import path

from .views import (
    AboutUsAPIView,
    MeContactAPIView,
    ServiceAPIView,
    PartnersAPIView,
    HomeBannerAPIView
    )


app_name = 'main'

urlpatterns = [
    path('hom/baner/', HomeBannerAPIView.as_view(), name='home'),
    path('about/', AboutUsAPIView.as_view(), name='about'),
    path('service/', ServiceAPIView.as_view(), name='service'),
    path('partners/', PartnersAPIView.as_view(), name='partners'),
    path('mecontact/', MeContactAPIView.as_view(), name='me_contact'),
]


'''
    AboutUs
        -list
    MeContact
        -list
    Service
        -list
    Partners
        -list
    HomeBanner
        -list
'''