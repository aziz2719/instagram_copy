from django.contrib import admin
from publications.models import Publications, PublicationImages, Likes, Comments


class PublicationImagesInline(admin.TabularInline):
    model = PublicationImages
    extra = 0

class PublicationsAdmin(admin.ModelAdmin):
    inlines = [PublicationImagesInline]
    readonly_fields = ('date',)

admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Likes)
admin.site.register(Comments)