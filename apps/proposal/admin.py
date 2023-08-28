# proposals/admin.py
from django.contrib import admin
from .models import CustomField, ProposalCustomField, Proposal

@admin.register(CustomField)
class CustomFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data_type')

@admin.register(ProposalCustomField)
class ProposalCustomFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_field', 'value_char', 'value_decimal')

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    filter_horizontal = ('custom_fields',)