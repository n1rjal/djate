from enum import Enum


class TaskStatus(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
