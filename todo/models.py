from django.db import models

class Todo(models.Model):
    complete = models.BooleanField(default=False)
    todotext = models.CharField(max_length=50)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.todotext
