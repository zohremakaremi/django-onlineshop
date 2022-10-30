from django.db import models
from django.urls import reverse
# Create your models here.

class Menu(models.Model):
	sub_menu = models.ForeignKey('self', on_delete=models.CASCADE, related_name='smenu', null=True, blank=True)
	is_sub = models.BooleanField(default=False)
	name = models.CharField(max_length=200)
	link=models.URLField(max_length=100)

	class Meta:
		
		verbose_name = 'منو'
		verbose_name_plural = 'منوها'

	def __str__(self):
		return self.name
