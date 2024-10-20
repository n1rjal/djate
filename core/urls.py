"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from todo.urls import urlpatterns as todo_urls
from . import logs

schema_view = get_schema_view(
    openapi.Info(
        title="Djate Api",
        default_version="v1",
        description="Djate API",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("logs/", logs.index_directory_log, name="logs-dir"),
    path("logs/<str:filename>", logs.serve_file, name="log-file"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "api/v1/",
        include(
            [
                #
                #
                #
                # v1 urls
                path("rester/", include("rester.urls")),
                path("todo/", include(todo_urls)),
            ]
        ),
    ),
]
