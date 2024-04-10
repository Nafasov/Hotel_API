from rest_framework import generics

from .models import (
    AboutUs,
    MeContact,
    Service,
    Partners,
    HomeBanner
    )

from .serializers import (
    AboutUsSerializer,
    MeContactSerializer,
    ServiceSerializer,
    PartnersSerializer,
    HomeBannerSerializer
    )


class AboutUsAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    pagination_class = None


class MeContactAPIView(generics.ListAPIView):
    queryset = MeContact.objects.all()
    serializer_class = MeContactSerializer
    pagination_class = None


class ServiceAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = None


class PartnersAPIView(generics.ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    pagination_class = None


class HomeBannerAPIView(generics.ListAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer
    pagination_class = None
