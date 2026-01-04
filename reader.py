import re

class ItemContainer:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "ItemContainer({" + self.path + "})"

    def GetItems(self):
        with open(self.path, "r", encoding="utf-8") as f:
            text = f.read()

        pattern = r"(option value=)(\"\b\w+\")(>)"

        options = re.findall(pattern, text)

        group2s = [match[1] for match in options]

        cleaned = [s.strip('"\'') for s in group2s]

        return cleaned