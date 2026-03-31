 🕷️ Django-cwh
 Web Scraper 

A Django-based web scraping and data tool. The project scrapes web data, processes it, and displays it through a Django web interface.


 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, SCSS, JavaScript |
| Database | SQLite (`db.sqlite3`) |


 📁 Project Structure

Django-cwh/
├── home/                      # Main Django app
├── myproject/                 # Django project settings
├── venv/                      # Virtual environment
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── fix_images.py              # Utility: fix image paths/links
├── fix_links.py               # Utility: fix broken links
├── image_update.py            # Utility: update image data
├── uncomment.py               # Utility script
└── update_static_tags.py      # Utility: update static file tags

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/rajvee123/Django-cwh.git
cd Django-cwh

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Open your browser and visit `http://127.0.0.1:8000`

