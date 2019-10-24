# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Feedback


admin.site.site_header ="FeedBook Admin Panel";
admin.site.site_title = "ACP - Feedbook";
admin.site.index_title = "Navigation";


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'feedback',)
    list_filter = ('date',)
    search_fields = ('customer_name', 'feedback',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
