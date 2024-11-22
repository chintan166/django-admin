from django.contrib import admin
from .models import Course,Lesson

admin.site.site_header = "chintan django custom header"

class LessionInline(admin.TabularInline):
    model = Lesson
    max_num = 5
    extra = 1
    exclude = ('video_url',)
    can_delete=True

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','published_date','price','full_title')
    #list_display_links = ('price','published_date')
    list_editable = ('published_date','price')
    list_filter = ('title','published_date',)
    search_fields = ('title',)
    readonly_fields = ('status',)
    inlines = (LessionInline,)
    
    #fields = ('title','published_date','status','author')
    fieldsets=(
        (None,{
          'fields':('title','published_date','price')  
        }),
        ('Extra info',{
            'classes':('collapse','wide'),
            'fields':('author','status')
        }))
    
    def full_title(self,obj):
        return f"{obj.title}-{obj.price}"
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','course')
    #list_filter = ('course__status')
    search_fields = ('title',)
    list_editable = ('course',)
    autocomplete_fields = ('course',)

admin.site.register(Course,CourseAdmin)
