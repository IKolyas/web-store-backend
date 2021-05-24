from django.contrib import admin
from django.contrib.auth.models import User
from userprofile.models import Profile


@admin.register(Profile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = (
        'user',
        'user_id',
        'gender',
        'birthday',
        'hometown',
        'balance',
        'create_at',
        'update_at',
        'avatar',
    )
    fields = [('user', 'avatar', ), ('gender', 'birthday',), ('hometown',),
              ('balance',)]
    list_filter = ('birthday',)
    # поиск по штрихкоду
    search_fields = ['user_id__startswith']
