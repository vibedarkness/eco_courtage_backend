from django.contrib import admin
from .models import Blog, Contact, Quotation

@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "created_at")
    list_filter = ("created_at", "author")
    search_fields = ("title", "content")
    date_hierarchy = "published_at"
    ordering = ("-published_at",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email","created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "email", "message")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "contract_type", "estimated_consumption", "created_at")
    list_filter = ("contract_type", "created_at")
    search_fields = ("full_name", "email", "message")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
