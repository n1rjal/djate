from django.urls import path, include
from . import views

urlpatterns = [
    # nested url patterns
    path(
        "tasks/",
        include(
            [
                path("list/", views.list_tasks, name="tasks-list"),
                path("create/", views.create_task, name="tasks-create"),
                path("get/<int:task_id>/", views.get_task, name="tasks-get"),
                path(
                    "update/<int:task_id>/",
                    views.update_task,
                    name="tasks-update",
                ),
                path(
                    "delete/<int:task_id>/",
                    views.delete_task,
                    name="tasks-delete",
                ),
            ]
        ),
        name="todo-tasks",
    ),
    path(
        "tags/",
        include(
            [
                path(
                    "list/",
                    views.TagViewSet.as_view({"get": "list"}),
                    name="tags-list",
                ),
                path(
                    "create/",
                    views.TagViewSet.as_view({"post": "create"}),
                    name="tags-create",
                ),
                path(
                    "get/<int:tag_id>/",
                    views.TagViewSet.as_view({"get": "retrieve"}),
                    name="tag-get",
                ),
                path(
                    "update/<int:tag_id>/",
                    views.TagViewSet.as_view({"patch": "update"}),
                    name="tag-update",
                ),
                path(
                    "delete/<int:tag_id>/",
                    views.TagViewSet.as_view({"delete": "destroy"}),
                    name="tag-delete",
                ),
            ]
        ),
        name="todo-tags",
    ),
]
