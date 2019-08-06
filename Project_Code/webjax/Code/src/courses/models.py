from django.db import models

# Create your models here.

class Course(models.Model):
	slug = models.SlugField()
	title = models.CharField(max_length=120)
	description = models.TextFiled()
	allowed_memberships = models.ManyToManyField(Membership)

	def __str__(self):
		return self.title
