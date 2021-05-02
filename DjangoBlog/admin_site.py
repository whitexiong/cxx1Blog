#!/usr/bin/env python
# encoding: utf-8


from django.contrib.admin import AdminSite
from DjangoBlog.utils import get_current_site
from django.contrib.sites.admin import SiteAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.sites.models import Site
from DjangoBlog.logentryadmin import LogEntryAdmin
from blog.admin import *
from accounts.admin import *
from oauth.admin import *
from servermanager.admin import *
from comments.admin import *
from owntracks.admin import *


class DjangoBlogAdminSite(AdminSite):
    site_header = 'DjangoBlog administration'
    site_title = 'DjangoBlog site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def get_queryset(self, request):  # 重写get_queryset
        qs = super(After_saleAdmin, self).get_queryset(request)
        if request.user.is_superuser:  # 判断如果是超级管理员返回所有信息
            return qs
        else:
            return qs.filter(User=request.user)  # User为当前关联的用户，如果是普通管理


    def has_permission(self, request):
        return request.user.is_superuser

    # def get_urls(self):
    #     urls = super().get_urls()
    #     from django.urls import path
    #     from blog.views import refresh_memcache
    #
    #     my_urls = [
    #         path('refresh/', self.admin_view(refresh_memcache), name="refresh"),
    #     ]
    #     return urls + my_urls


admin_site = DjangoBlogAdminSite(name='admin')

admin_site.register(Article, ArticlelAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Links, LinksAdmin)
admin_site.register(SideBar, SideBarAdmin)
admin_site.register(BlogSettings, BlogSettingsAdmin)

admin_site.register(commands, CommandsAdmin)
admin_site.register(EmailSendLog, EmailSendLogAdmin)

admin_site.register(BlogUser, BlogUserAdmin)

admin_site.register(Comment, CommentAdmin)

admin_site.register(OAuthUser, OAuthUserAdmin)
admin_site.register(OAuthConfig, OAuthConfigAdmin)

admin_site.register(OwnTrackLog, OwnTrackLogsAdmin)

admin_site.register(Site, SiteAdmin)

admin_site.register(LogEntry, LogEntryAdmin)

