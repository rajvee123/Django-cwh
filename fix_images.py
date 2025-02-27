import os
import re

# Path to your templates folder
templates_folder = 'myproject/templates'

# Function to update the <img> tags in a single file
def update_img_tags(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Regular expression to match <img> tags and update their src attributes
        updated_content = re.sub(
            r'(<img[^>]+src=")(?!{% static)([^"]+)(")', 
            r'\1{% static "\2" %}\3', 
            content
        )

        # Save the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Updated image tags in: {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

# Function to iterate over all HTML files in the templates folder
def update_all_html_files():
    for root, dirs, files in os.walk(templates_folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                update_img_tags(file_path)

# Run the script
if __name__ == "__main__":
    update_all_html_files()
