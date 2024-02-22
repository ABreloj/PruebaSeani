from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Module(models.Model):
    name = models.CharField(verbose_name = 'Module names', max_length = 30)
    description = models.CharField(verbose_name = 'Modules description', max_length = 123456789)

    def num_questions(self):
        return self.question_set.count()
    num_questions.short_description = 'Numero de preguntas'
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'module'
        verbose_name_plural = 'modulos'
    

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    question_text = models.CharField( null = True, blank = True, verbose_name = 'La preguta...LA PREGUNTA :O', max_length = 52)
    #question_image = models.ImageField(null = True, blank = True, verbose_name = 'Imagen de la pregunta', upload_to = 'questions')
    question_image = CloudinaryField(null = True, blank = True, verbose_name = 'Imagen de la pregunta', resource_type = 'image', folder = 'questions' )
    answer1 = models.CharField(verbose_name = '1', max_length = 200)
    answer2 = models.CharField(verbose_name = '2', max_length = 200)
    answer3 = models.CharField(null = True, blank = True, verbose_name = '3', max_length = 200)
    answer4 = models.CharField(null = True, blank = True, verbose_name = '4', max_length = 200)
    correct = models.CharField(verbose_name = 'La respuesta siiii uwu', max_length = 8)

    def __str__(self):
        return f"{ self.module } Pregunta { self.id}"
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'