import os
import re

# Path to your templates folder
templates_folder = 'myproject/templates'  # Update this if the path is different

# Function to update image tags to use {% static %}
def update_image_tags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex to find <img> tags with src attributes starting with 'img/' or relative paths
    updated_content = re.sub(
        r'<img\s+([^>]*\s+src=["\'])([^"\']+)(["\'][^>]*>)',
        r'<img \1{% static "\2" %}\3',
        content
    )

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Walk through all HTML files in the templates folder
for root, dirs, files in os.walk(templates_folder):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            update_image_tags(file_path)

print("All image tags updated to use {% static %} successfully!")
