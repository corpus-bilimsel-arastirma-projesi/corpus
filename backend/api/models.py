from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=50, null=False, default="old")

    def as_dict(self):
        return {
            "id": self.id,
            "filename": str(self.file)
        }
