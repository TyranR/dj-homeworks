from django.contrib import admin

# Register your models here.

from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Phone, PhoneAdmin)