from django.db import models
from django.urls import reverse

# Create your models here.
STATUS =(
	(0,'Drat'),
	(1,'Publish')
	)

class Article(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(null=False,unique=True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True) 
	updated_on = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS,default=0)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('article-detail', kwargs={'slug':self.slug})