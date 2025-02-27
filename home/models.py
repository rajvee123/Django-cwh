from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField(max_length=122)
    
    def __str__(self):
        return self.name

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    room_no = models.CharField(max_length=10)
    mis = models.CharField(max_length=15, unique=True)  # Used as Username
    phone = models.CharField(max_length=15,unique=True)  # Used as Password
    dob = models.DateField()
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.mis})"


from django.db import models
from django.utils.timezone import now

class AbsenteeRecord(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=[("lunch", "Lunch"), ("dinner", "Dinner")])
    marked_at = models.DateTimeField(auto_now_add=True)  # Store when it was marked

    def __str__(self):
        return f"{self.student.name} - {self.meal_type} - {self.date}"
    
    from django.db import models
from django.utils.timezone import now

class MealPrice(models.Model):
    date = models.DateField(unique=True, default=now)  # Admin enters meal price daily
    lunch_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    dinner_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.date} - Lunch: ₹{self.lunch_price}, Dinner: ₹{self.dinner_price}"


    
