import re

text = """
Hello, my email is ali@gmail.com.
You can contact mitadt@yahoo.com.
My college email is ali123@gmail.com.
For support, contact support@company.org.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)
