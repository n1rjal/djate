from . import settings
import os
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


@user_passes_test(lambda user: user.is_superuser)
def index_directory_log(request):
    files = os.listdir(settings.LOG_ROOT)
    return render(request, "logs/index.html", {"files": files})


@user_passes_test(lambda user: user.is_superuser)
def serve_file(request, filename):
    log_dir = settings.LOG_ROOT
    file_path = os.path.join(log_dir, filename)
    with open(file_path) as f:
        response = HttpResponse(f.read(), content_type="text/plain")
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
