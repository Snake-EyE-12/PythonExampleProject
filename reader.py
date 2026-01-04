import re

file_path = "All Items"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r"\b\w+\b", text)

print(f"Found {len(words)} words:")
print(words)