from django.contrib import admin
from django.contrib.auth.models import User
from userprofile.models import Profiles


@admin.register(Profiles)
class AdminUserProfile(admin.ModelAdmin):
    list_display = (
        'user_id',
        'gender',
        'birthday',
        'hometown',
        'balance',
        'create_at',
        'update_at'
    )
    fields = [('user_id', 'gender', 'birthday',), ('hometown',),
              ('balance',)]
    list_filter = ('birthday',)
    # поиск по штрихкоду
    search_fields = ['user_id__startswith']
