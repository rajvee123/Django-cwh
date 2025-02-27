import re

# Read the base.html file from the myproject/templates directory
# with open('myproject/templates/base.html', 'r') as file:
#     content = file.read()

# # Regex to find image tags and update them to use {% static %} tag
# updated_content = re.sub(r'src="(img/[^"]+)"', r'src="{% static "\1" %}"', content)

# Write the updated content back to a new file in the templates directory
with open('myproject/templates/base_updated.html', 'w') as file:
    file.write(updated_content)

print("base.html updated successfully!")
