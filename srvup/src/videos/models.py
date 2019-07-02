from django.db import models

# Create your models here.


class Video(models.Model):
	title      = models.CharField(max_length=120)
	embed_code = models.TextField()
	timestamp  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.embed_code  