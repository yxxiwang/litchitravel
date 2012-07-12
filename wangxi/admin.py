from django.contrib import admin
from wangxi.models import Member,Message

admin.site.register(Member)
admin.site.register(Message)
admin.site.index_template = 'index.html'
#admin.site.index_template = 'wangxi/index.html'
