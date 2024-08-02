from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(logo)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','banner_image')

@admin.register(mains)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo')