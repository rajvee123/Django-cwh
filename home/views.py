from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect  # ✅ Ensure render is imported
from django.contrib import messages
from .forms import RegisterForm
from django.utils.timezone import now



# Create your views here.
def index(request):
    return render(request, 'index.html') 
def about(request):
    return render(request, 'about.html') 
def booking(request):
    return render(request, 'booking.html')
def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email, subject = subject,
        message = message)
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request, 'contact.html')
def menu(request):
    return render(request, 'menu.html')   
def service(request):
    return render(request, 'service.html') 
def team(request):
    return render(request, 'team.html') 
def testimonial(request):
    return render(request, 'testimonial.html') 

from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Student
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to login after successful registration
        else:
            messages.error(request, "Error in form submission. Please check your details.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})  # ✅ Ensure render is correctly used


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student  # Ensure this import exists

def login_view(request):  # ✅ Ensure this function name matches exactly
    if request.method == "POST":
        mis = request.POST.get("mis")
        phone = request.POST.get("phone")

        try:
            student = Student.objects.get(mis=mis, phone=phone)
            request.session["student_id"] = student.id  # Store session
            messages.success(request, f"Welcome, {student.name}!")
            return redirect("dashboard")  # Redirect to dashboard after login
        except Student.DoesNotExist:
            messages.error(request, "Invalid MIS or Phone Number.")

    return render(request, "login.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def login_view(request):
    if request.method == "POST":
        mis = request.POST.get("mis")
        phone = request.POST.get("phone")

        try:
            student = Student.objects.get(mis=mis, phone=phone)
            request.session["student_id"] = student.id  # Store session
            messages.success(request, f"Welcome, {student.name}!")
            return redirect("dashboard")  # Redirect to dashboard after login
        except Student.DoesNotExist:
            messages.error(request, "Invalid MIS or Phone Number.")

    return render(request, "login.html")

# def dashboard(request):
#     # Check if user is logged in (session exists)
#     student_id = request.session.get("student_id")
#     if not student_id:
#         messages.error(request, "You must be logged in to access the dashboard.")
#         return redirect("login")  # Redirect to login if not logged in

#     # Get student details
#     student = Student.objects.get(id=student_id)

#     return render(request, "dashboard.html", {"student": student})

# def logout_view(request):
#     request.session.flush()  # Clear user session
#     messages.success(request, "You have been logged out successfully.")
#     return redirect("login")  # Redirect to login page

def dashboard(request):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "You must be logged in to access the dashboard.")
        return redirect("login")

    student = Student.objects.get(id=student_id)
    today = now().date()
    current_month = today.strftime("%B %Y")  # Example: "February 2025"

    # Calculate the mess bill
    mess_bill = calculate_mess_bill(student)

    return render(request, "dashboard.html", {
        "student": student,
        "mess_bill": mess_bill,
        "current_month": current_month
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from datetime import datetime, time, timedelta
from .models import Student, AbsenteeRecord
from django.db.models import Count



from datetime import datetime, timedelta

def mark_multiple_absent(request):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "You must be logged in.")
        return redirect("login")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        start_date = request.POST.get("start_date")
        start_meal = request.POST.get("start_meal")
        end_date = request.POST.get("end_date")
        end_meal = request.POST.get("end_meal")

        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if start_date > end_date:
            messages.error(request, "Start date cannot be after end date.")
            return redirect("dashboard")

        # Generate all meals between the given range
        meal_types = ["lunch", "dinner"]
        absentees = []
        for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days + 1)):
            for meal in meal_types:
                if (single_date == start_date and meal == start_meal) or (single_date == end_date and meal == end_meal) or (start_date < single_date < end_date):
                    absentees.append((single_date, meal))

        # Check if the user is exceeding 16 absences in the month
        current_month_start = now().date().replace(day=1)
        absentee_count = AbsenteeRecord.objects.filter(student=student, date__gte=current_month_start).count()
        if absentee_count + len(absentees) > 16:
            messages.error(request, "You are exceeding the 16 absences per month limit.")
            return redirect("dashboard")

        # Save all absences
        for date, meal in absentees:
            AbsenteeRecord.objects.create(student=student, date=date, meal_type=meal)

        messages.success(request, "Successfully marked absent for selected days.")
        return redirect("dashboard")

    return redirect("dashboard")


from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from datetime import time
from .models import Student, AbsenteeRecord
from django.db.models import Count

from django.utils.timezone import localtime

def mark_absent(request, meal_type):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "You must be logged in.")
        return redirect("login")

    student = Student.objects.get(id=student_id)
    today = localtime(now()).date()  # Get current date in IST
    current_time = localtime(now()).time()  # Get current time in IST

    # Meal cut-off times
    lunch_deadline = time(9, 0)  # 9 AM IST
    dinner_deadline = time(18, 0)  # 6 PM IST

    print(f"Current Time: {current_time}")  # Debugging
    print(f"Checking Absentee for: {meal_type}")

    # Check if it's past the deadline
    if (meal_type == "lunch" and current_time > lunch_deadline) or (meal_type == "dinner" and current_time > dinner_deadline):
        messages.error(request, f"You can only mark {meal_type} absent before {lunch_deadline if meal_type == 'lunch' else dinner_deadline}.")
        return redirect("dashboard")

    # Check if already marked absent
    if AbsenteeRecord.objects.filter(student=student, date=today, meal_type=meal_type).exists():
        messages.warning(request, f"You have already marked {meal_type} absent for today.")
        return redirect("dashboard")

    # Save the absentee record
    AbsenteeRecord.objects.create(student=student, date=today, meal_type=meal_type)
    messages.success(request, f"You are now marked absent for {meal_type} on {today}.")
    return redirect("dashboard")


def undo_absent(request, meal_type):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "You must be logged in.")
        return redirect("login")

    student = Student.objects.get(id=student_id)
    today = now().date()
    current_time = now().time()

    # Meal cut-off times
    lunch_deadline = time(9, 0)  # 9 AM IST
    dinner_deadline = time(18, 0)  # 6 PM IST

    # Check if it's past the deadline
    if (meal_type == "lunch" and current_time > lunch_deadline) or (meal_type == "dinner" and current_time > dinner_deadline):
        messages.error(request, f"You can only undo {meal_type} absence before {lunch_deadline if meal_type == 'lunch' else dinner_deadline}.")
        return redirect("dashboard")

    # Delete the absentee record if it exists
    absentee = AbsenteeRecord.objects.filter(student=student, date=today, meal_type=meal_type)
    if absentee.exists():
        absentee.delete()
        messages.success(request, f"Your absence for {meal_type} on {today} has been removed.")
    else:
        messages.warning(request, f"You were not marked absent for {meal_type} today.")

    return redirect("dashboard")

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_absentee_report(request):
    today = now().date()
    lunch_absentees = AbsenteeRecord.objects.filter(date=today, meal_type="lunch").count()
    dinner_absentees = AbsenteeRecord.objects.filter(date=today, meal_type="dinner").count()

    return render(request, "admin_absentee_report.html", {
        "lunch_absentees": lunch_absentees,
        "dinner_absentees": dinner_absentees
    })

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_absentee_report(request):
    today = now().date()

    # Get total count
    lunch_absentees_count = AbsenteeRecord.objects.filter(date=today, meal_type="lunch").count()
    dinner_absentees_count = AbsenteeRecord.objects.filter(date=today, meal_type="dinner").count()

    # Get list of absent students
    lunch_absentees = AbsenteeRecord.objects.filter(date=today, meal_type="lunch").select_related("student")
    dinner_absentees = AbsenteeRecord.objects.filter(date=today, meal_type="dinner").select_related("student")

    return render(request, "admin_absentee_report.html", {
        "lunch_absentees_count": lunch_absentees_count,
        "dinner_absentees_count": dinner_absentees_count,
        "lunch_absentees": lunch_absentees,
        "dinner_absentees": dinner_absentees,
    })

def dashboard(request):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "You must be logged in to access the dashboard.")
        return redirect("login")

    student = Student.objects.get(id=student_id)
    today = now().date()
    current_month_start = today.replace(day=1)

    # Fetch absentee records
    absentee_records = AbsenteeRecord.objects.filter(student=student, date__gte=current_month_start)

    # Count absentees in the current month
    total_absentees = absentee_records.count()
    remaining_absentees = max(16 - total_absentees, 0)  # Prevent negative values

    return render(request, "dashboard.html", {
        "student": student,
        "absentee_records": absentee_records,
        "remaining_absentees": remaining_absentees
    })

def calculate_mess_bill(student):
    today = now().date()
    start_of_month = today.replace(day=1)

    # Get all absentee records for this student in the current month
    absences = AbsenteeRecord.objects.filter(student=student, date__gte=start_of_month)

    # Get all meal prices for the month
    meal_prices = MealPrice.objects.filter(date__gte=start_of_month)
    meal_prices_dict = {meal.date: meal for meal in meal_prices}

    total_bill = 0

    for meal in meal_prices:
        meal_cost = 0

        if meal.date not in [a.date for a in absences if a.meal_type == "lunch"]:
            meal_cost += meal.lunch_price  # Add lunch price if not absent

        if meal.date not in [a.date for a in absences if a.meal_type == "dinner"]:
            meal_cost += meal.dinner_price  # Add dinner price if not absent

        total_bill += meal_cost  # Add the calculated price for that day

    return total_bill

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_mess_bill_report(request):
    students = Student.objects.all()
    student_bills = {student: calculate_mess_bill(student) for student in students}

    return render(request, "admin_mess_bill_report.html", {
        "student_bills": student_bills
    })

from django.shortcuts import redirect
from django.contrib import messages

def logout_view(request):
    request.session.flush()  # ✅ Clears the session (logs out the user)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")  # ✅ Redirect to login page

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        room_no = request.POST.get("room_no")
        mis = request.POST.get("mis")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        year = request.POST.get("year")
        branch = request.POST.get("branch")

        # Check if user already exists
        if Student.objects.filter(mis=mis).exists():
            messages.error(request, "A student with this MIS already exists.")
            return redirect("register")

        # Create new student
        Student.objects.create(
            name=name, email=email, room_no=room_no, mis=mis,
            phone=phone, dob=dob, year=year, branch=branch
        )

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, "register.html")






