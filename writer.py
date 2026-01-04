class Generator:
    def Give(self, text):
        return "give @s minecraft:" + text

    def Roll(self, size):
        return "random roll 1.." + size

    def Generate(self, pattern):
        return "done"






with open("output.txt", "w", encoding="utf-8") as output:
    output.write("Hello world\n")
