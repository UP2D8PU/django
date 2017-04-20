from django.contrib import admin

# Register your models here.
 
from .models import Product, Feedback
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback', 'name', 'date', 'happy',)
    list_filter = ('feedback', 'date',)
    search_fields = ('product__name', 'details',)
 
    class Meta:
        model = Feedback
 
 
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Product)
