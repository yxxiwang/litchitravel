from django.contrib import admin
from wangxi.models import Member

admin.site.register(Member)
admin.site.index_template = 'index.html'
#admin.site.index_template = 'wangxi/index.html'
