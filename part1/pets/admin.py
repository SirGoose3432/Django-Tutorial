from django.contrib import admin

from .models import Pet, Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner', 'age')

admin.site.register(Pet, PetAdmin)
admin.site.register(Owner, OwnerAdmin)
