from django.contrib import admin
from .models import Contact
from django.contrib import messages
from django.utils.translation import ngettext


@admin.action(description="Set the status as Open")
def status_open(modeladmin, request, queryset):
    updated = queryset.update(status="OPEN")
    modeladmin.message_user(
        request,
        ngettext(
            "%d ticket was successfully marked as Open.",
            "%d tickets were successfully marked as Open.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="Set the status as In Progress")
def status_in_progress(modeladmin, request, queryset):
    updated = queryset.update(status="IN_PROGRESS")  # You also missed defining `updated`
    modeladmin.message_user(
        request,
        ngettext(
            "%d ticket was successfully marked as In Progress.",
            "%d tickets were successfully marked In Progress.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="Set the status as Closed")
def status_closed(modeladmin, request, queryset):
    updated = queryset.update(status="CLOSED")
    modeladmin.message_user(
        request,
        ngettext(
            "%d ticket was successfully marked as Closed.",
            "%d tickets were successfully marked as Closed.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'subject', 'timestamp', 'status']
    list_filter = ['status', 'timestamp', 'name', 'email', 'subject', 'phone_number']
    actions = [status_open, status_in_progress, status_closed]
    search_fields = ['name', 'email', 'phone_number',
                     'subject', 'timestamp', 'status']
