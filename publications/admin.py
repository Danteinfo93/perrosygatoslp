from django.contrib import admin
from .models import Profile, Trainer, Ad, Adoption, Straying, Finding, Cross, Breed, Location
# Register your models here.

class AdoptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Profile)
admin.site.register(Trainer)
admin.site.register(Ad)
admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Straying)
admin.site.register(Finding)
admin.site.register(Cross)
admin.site.register(Breed)
admin.site.register(Location)