from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(published=True)


class Entry(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200, default="")
	body = RichTextField(config_name='default')
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return 'posts:entry', (self.slug())



	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
