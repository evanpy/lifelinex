from django.db import models

# Create your models here.
class Session(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    counsellorChatId = models.CharField(max_length=50, null=False, blank=False)
    clientChatId = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
