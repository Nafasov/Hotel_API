from django.contrib import admin

from .models import (
    RoomServices,
    Rooms,
    RoomContent,
    RoomImages,
    Booking,
    RoomComments,
    )


@admin.register(RoomServices)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


class RoomContentAdmin(admin.TabularInline):
    model = RoomContent
    extra = 1


class RoomImagesAdmin(admin.TabularInline):
    model = RoomImages
    extra = 1


@admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    inlines = (RoomContentAdmin, RoomImagesAdmin)
    list_display = ('id', 'title', 'created_date')
    search_fields = ('id', 'title')
    date_hierarchy = 'created_date'
    list_per_page = 10
    filter_horizontal = ('services', )


@admin.register(RoomComments)
class RoomCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'author', 'created_date')
    search_fields = ('id', 'author', 'room')
    date_hierarchy = 'created_date'
    list_per_page = 20


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', )