import os
import re

# Define the path to your templates folder
TEMPLATES_DIR = "myproject/templates"  # Change if your path is different

# Define mapping of pages to Django URL names
URL_MAPPING = {
    "index.html": "index",
    "about.html": "about",
    "menu.html": "menu",
    "service.html": "service",
    "contact.html": "contact",
    "team.html": "team",
    "testimonial.html": "testimonial",
    "account.html": "account",
    "booking.html": "booking"
}

# Regex pattern to match hardcoded links like href="about.html"
pattern = re.compile(r'href="([\w-]+\.html)"')

def fix_links_in_file(file_path):
    """Replace hardcoded HTML links with Django {% url %} tags."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and replace hardcoded links
    modified_content = pattern.sub(lambda match: f'href="{{% url \'{URL_MAPPING.get(match.group(1), "#") }\' %}}"', content)

    # Save changes only if modifications were made
    if content != modified_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print(f"✅ Fixed links in {file_path}")

def scan_templates():
    """Scan all HTML files in templates directory and fix links."""
    for root, _, files in os.walk(TEMPLATES_DIR):
        for file in files:
            if file.endswith(".html"):
                fix_links_in_file(os.path.join(root, file))

if __name__ == "__main__":
    scan_templates()
    print("🎉 All hardcoded links have been updated to Django {% url %} format!")
