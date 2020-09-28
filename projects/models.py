from django.db import models
from django.utils.timezone import now


class Project(models.Model):

    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=885)
    meta = models.JSONField()
    image = models.ImageField(upload_to='projects')
    order = models.SmallIntegerField()
    alt = models.CharField(max_length=255)
    started = models.DateField(default=now)
    views = models.BigIntegerField(default=0)
    dest = models.URLField()
    repo = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'proj id: {self.project_id}, {self.title}'
