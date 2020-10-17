from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Project(models.Model):
    site_name_caps = str("BOTNIO")
    site_name_reg = str("Botnio")
    site_name_low = str("botnio")

    def categories_processor(request):
        categories = Project.objects.all()            
        return {'categories': categories}