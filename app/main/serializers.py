from rest_framework import serializers

from .models import (
    AboutUs,
    MeContact,
    Service,
    Partners,
    HomeBanner
    )


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'image', 'content']


class MeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeContact
        fields = ['id', 'phone', 'email', 'facebook', 'linkedin', 'twitter', 'instagram', 'address', 'open_time', 'close_time']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'image']


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['id', 'name', 'image', 'url']


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = ['id', 'title', 'image', 'description']
