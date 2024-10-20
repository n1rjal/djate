from django.contrib import admin
from .models import Task, Tag

# Register your models here.


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "get_tags",
        "completed",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "completed")
    list_filter = ("completed", "created_at", "updated_at")
    autocomplete_fields = ("tags",)

    def get_tags(self, obj):
        return [tag for tag in obj.tags.all()]

    get_tags.short_description = "tags"
