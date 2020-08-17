from django.contrib import admin
from .models import Post,Profile,HotTake,Source
# Register your models here.

class SourceInline(admin.TabularInline):
    model = Source

class HotTakeAdmin(admin.ModelAdmin):
    inlines = [
        SourceInline,
    ]

admin.site.register(Post)
admin.site.register(HotTake)
admin.site.register(Source)
admin.site.register(Profile)