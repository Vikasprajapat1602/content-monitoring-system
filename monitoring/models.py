from django.db import models


# Keyword Model
class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# ContentItem Model
class ContentItem(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    source = models.CharField(max_length=255)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.title


# Flag Model
class Flag(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('relevant', 'Relevant'),
        ('irrelevant', 'Irrelevant'),
    ]

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)

    score = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # for suppression logic
    last_reviewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.keyword} - {self.content_item} ({self.status})"