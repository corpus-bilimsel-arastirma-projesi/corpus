from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=100)
    json = models.TextField(default='Json', null=False)
    edited_json = models.TextField(default='Json', blank=True)

    def as_dict(self):
        return {
            "id": self.id,
            "filename": self.file_name,
            "date": self.date,
        }
