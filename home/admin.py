from django.contrib import admin
from home.models import Contact
# Register your models here.
admin.site.register(Contact)
from django.contrib import admin
from .models import Student
from django.utils.timezone import now


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mis', 'email', 'phone', 'year', 'branch')  # Columns to display
    search_fields = ('name', 'mis', 'email')  # Searchable fields
    list_filter = ('year', 'branch')  # Filter options

from django.contrib import admin
from .models import Student, AbsenteeRecord


@admin.register(AbsenteeRecord)
class AbsenteeRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'meal_type', 'marked_at')
    search_fields = ('student__name', 'student__mis')
    list_filter = ('meal_type', 'date')

    def get_queryset(self, request):
        """Show absentees in the admin panel for today only"""
        qs = super().get_queryset(request)
        today = now().date()
        return qs.filter(date__gte=today.replace(day=1))  # Show only current month absentees

from .models import MealPrice

@admin.register(MealPrice)
class MealPriceAdmin(admin.ModelAdmin):
    list_display = ('date', 'lunch_price', 'dinner_price')
    list_filter = ('date',)
    search_fields = ('date',)


