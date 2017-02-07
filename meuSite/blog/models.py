from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') # este e um link para outro modelo
    title = models.CharField(max_length=200) # assim e como voce define um texto com um numero limitado de caracteres
    text = models.TextField() #este e para textos longos sem um limite
    created_date = models.DateTimeField(default=timezone.now) #este  uma data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # def:  significa que se trata de um funcao/metodo  - --  publish ' o nome do metodo'
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
