from django.db import models

from django.db import models

class UserResponse(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()
    session_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question}: {self.response}"

