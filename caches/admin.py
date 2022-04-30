from django.contrib import admin
from caches.models import Session, Cache, Clue


class SessionAdmin(admin.ModelAdmin):
    pass

class CacheAdmin(admin.ModelAdmin):
    pass

class ClueAdmin(admin.ModelAdmin):
    pass


admin.site.register(Session, SessionAdmin)

admin.site.register(Cache, CacheAdmin)

admin.site.register(Clue, ClueAdmin)