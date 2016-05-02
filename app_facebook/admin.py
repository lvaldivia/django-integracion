from django.contrib import admin

from app_facebook.models import User, UserScores,Settings

admin.site.register(User)
admin.site.register(UserScores)
admin.site.register(Settings)
