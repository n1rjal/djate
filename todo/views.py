from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer, TagSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import Task, Tag

# using class based approach


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()

    def get_object(self):
        tag_id = self.kwargs.get("tag_id")
        return Tag.objects.filter(pk=tag_id).first()


# using functional approach


@swagger_auto_schema(
    method="GET",
    responses={status.HTTP_200_OK: TaskSerializer},
    operation_description="Get all tasks",
)
@api_view(["GET"])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(
        serializer.data,
    )


@swagger_auto_schema(
    method="POST",
    request_body=TaskSerializer,
    responses={status.HTTP_201_CREATED: TaskSerializer},
    operation_description="Create a task",
)
@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        serializer.data,
    )


@swagger_auto_schema(
    method="GET",
    responses={status.HTTP_200_OK: TaskSerializer},
    operation_description="Get a task by id",
)
@api_view(["GET"])
def get_task(request, **kwargs):
    task_id = kwargs.get("task_id")
    task = Task.objects.get(pk=task_id)
    serializer = TaskSerializer(task)
    return Response(
        serializer.data,
    )


@swagger_auto_schema(
    method="PATCH",
    request_body=TaskSerializer,
    responses={status.HTTP_200_OK: TaskSerializer},
    operation_description="Update a task by id",
)
@api_view(["PATCH"])
def update_task(request, **kwargs):
    task_id = kwargs.get("task_id")
    instance = Task.objects.get(pk=task_id)
    serializer = TaskSerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        serializer.data,
    )


@swagger_auto_schema(
    method="DELETE",
    responses={status.HTTP_204_NO_CONTENT: "deleted successfully"},
    operation_description="Delete a task by id",
)
@api_view(["DELETE"])
def delete_task(request, **kwargs):
    task_id = kwargs.get("task_id")
    task = Task.objects.get(pk=task_id)
    task.delete()
    return Response(
        {"deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
