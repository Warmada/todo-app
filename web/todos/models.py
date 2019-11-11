from django.db import models

class Todo(models.Model):
	todo = models.CharField(max_length=100, help_text='Obrigatório preencher o Todo')
	done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	closed_at = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.todo