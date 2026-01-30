from django.db import models

# Create your models here.
class short_urls(models.Model):
    orginal_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=10,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    visit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.orginal_url} --> {self.short_url}"
    