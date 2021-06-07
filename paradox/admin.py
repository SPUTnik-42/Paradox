from django.contrib import admin
from .models import team_member, question, log, hint, user_detail, User
# Register your models here.

admin.site.register(team_member)
#admin.site.register(team)
admin.site.register(question)
admin.site.register(log)
admin.site.register(hint)
admin.site.register(user_detail)
admin.site.register(User)