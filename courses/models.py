from django.db import models
from accounts.models import Account
import uuid


class COURSE_STATUS(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11,
        choices=COURSE_STATUS.choices,
        default=COURSE_STATUS.NOT_STARTED
    )
    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
    )

    students = models.ManyToManyField(
        Account,
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
