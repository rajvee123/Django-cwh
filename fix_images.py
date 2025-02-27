import os
import re

# Path to your templates folder (Change this to your actual path)
TEMPLATES_DIR = "myproject/templates"

def update_img_tags(file_path):
    """Updates only local image src paths to use Django's static template tag."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Regex to find local images (e.g., src="img/logo.png") but ignore external links (http, https)
        updated_content = re.sub(
            r'(<img[^>]+src=["\'])(?!http|https|/{% static)(img/[^"\']+)(["\'])',
            r'\1{% static "\2" %}\3',
            content
        )

        # Write the updated content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"✅ Updated: {file_path}")
    
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")

def update_all_templates():
    """Goes through all HTML files in the templates directory and updates image paths."""
    for root, _, files in os.walk(TEMPLATES_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                update_img_tags(file_path)

if __name__ == "__main__":
    update_all_templates()
    print("🚀 All image paths updated successfully!")
