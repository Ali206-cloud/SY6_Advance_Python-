import re

html_text = """
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a paragraph.</p>
    <div>This is a division.</div>
    <table>
        <tr>
            <td>Name</td>
            <td>Age</td>
        </tr>
    </table>
</body>
</html>
"""

pattern = r"<(h1|p|div|table)\b[^>]*>"

tags = re.findall(pattern, html_text, re.IGNORECASE)

print("HTML Tags Found:")
print("---")

for tag in tags:
    print("<" + tag + ">")

print("\nTotal tags found:", len(tags))