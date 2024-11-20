from django.db import models

class Course(models.Model):
    COURSE_STATUS=(
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    published_date = models.DateTimeField()
    price = models.IntegerField()
    author = models.CharField(max_length=200)
    status = models.CharField(default='published',help_text="enter field contain",max_length=200,choices=COURSE_STATUS)
    
    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)