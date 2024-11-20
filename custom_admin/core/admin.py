from django.contrib import admin
from .models import Course,Lesson

admin.site.site_header = "chintan django custom header"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','published_date','price','full_title')
    list_display_links = ('price','published_date')
    #fields = ('title','published_date','status','author')
    fieldsets=(
        (None,{
          'fields':('title','published_date')  
        }),
        ('Extra info',{
            'classes':('collapse','wide'),
            'fields':('author','status')
        }))
    
    def full_title(self,obj):
        return f"{obj.title}-{obj.price}"
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
   pass
    

admin.site.register(Course,CourseAdmin)
