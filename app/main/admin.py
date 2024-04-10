from django.contrib import admin

from .models import (
    AboutUs,
    MeContact,
    Service,
    Partners,
    HomeBanner
    )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(MeContact)
class MeContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
