# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now
from enum import Enum

# 待辦清單-完成狀態
class TodoStatus(Enum):
    UNFINISHED = 0
    FINISHED = 1


class Todolist(models.Model):
    COMPLETED_STATUS = (
        (TodoStatus.UNFINISHED, 'unfinish'),
        (TodoStatus.FINISHED,   'finish')
    )

    todo_id = models.AutoField(primary_key=True)
    completed = models.IntegerField(
        choices=COMPLETED_STATUS)  # 0 = False, 1 = True
    todo = models.CharField(max_length=20)
    last_update = models.DateTimeField(default=now)

    class Meta:
        # managed = False
        db_table = 'todolist'

    def isCompleted(self):
        if self.completed == TodoStatus.FINISHED.value:
            return True
        else:
            return False
