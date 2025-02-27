import os
import re

# Path to your templates folder
templates_folder = 'myproject/templates'  # Update this if the path is different

# Function to uncomment image tags
def uncomment_image_tags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex to find commented <img> tags and uncomment them
    updated_content = re.sub(r'<!--\s*(<img[^>]+>)\s*-->', r'\1', content)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Walk through all HTML files in the templates folder
for root, dirs, files in os.walk(templates_folder):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            uncomment_image_tags(file_path)

print("All image tags uncommented successfully!")
