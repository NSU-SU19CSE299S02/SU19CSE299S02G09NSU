from django.db import models

# Create your models here.

class Video(models.Model):
	embade_code = models.TextField()

	def __str__(self):
		return self.embade_code

## model migrate
