# 🍽️ COEP Mess Management System
> A Django-based internal web tool to digitize hostel mess operations at COEP — reducing paperwork and automating attendance, billing, and menu management.


## 📌 About

This is an internal mess management tool built for COEP's hostel facility. It replaces manual registers and paperwork with a simple web interface where students can mark absentees, check meal prices, and pay their monthly mess bill — all in one place.

> Built with guidance from the [Code With Harry](https://www.youtube.com/@CodeWithHarry) Django series.

---

## ✨ Features

- 🔐 **User Authentication** — Separate login for students and admins
- ✅ **Absentee Marking** — Students can mark themselves absent for meals
- 🍛 **Meal Price Checker** — View current meal rates
- 💸 **Monthly Billing** — Auto-calculated bills based on attendance
- 📋 **Menu Management** — Admins can update the mess menu
- 📄 **Paperwork Reduction** — Everything managed digitally, no registers needed

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, SCSS, JavaScript |
| Database | SQLite (`db.sqlite3`) |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/rajvee123/Django-cwh.git
cd Django-cwh
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```
Django-cwh/
├── home/               # Main app — views, models, templates
├── myproject/          # Django project settings & URLs
├── venv/               # Virtual environment (not tracked)
├── db.sqlite3          # SQLite database
├── manage.py           # Django entry point
├── fix_images.py       # Utility script for image fixes
├── fix_links.py        # Utility script for link fixes
├── image_update.py     # Image update helper
└── update_static_tags.py  # Static tag updater
```

---

## 👥 Roles & Access

| Feature | Student | Admin |
|---|:---:|:---:|
| Login / Logout | ✅ | ✅ |
| Mark Absentee | ✅ | ✅ |
| View Meal Prices | ✅ | ✅ |
| View Monthly Bill | ✅ | ✅ |
| Manage Billing | ❌ | ✅ |
| Update Menu | ❌ | ✅ |

---


---

*Built at COEP Technological University, Pune. Inspired by the Code With Harry Django series.*
