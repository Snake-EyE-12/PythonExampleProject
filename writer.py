from pathlib import Path

from optimizer import Optimization


class Generator:
    def Give(self, text):
        return "give @s minecraft:" + text

    def Roll(self, size):
        return "execute store result storage random:roll value int 1 run random value 1.." + size

    def Value(self, value):
        return "execute if data storage random:roll {value:"+value+"}"

    def TreeDepth(self, depth, group): #depth0group0
        return "function game:items/depth"+depth+"group"+group

    def FullRandomGive(self, value, text):
        return self.Value(value) + " run " + self.Give(text)

    def FullRandomDepth(self, value, depth, group):
        return self.Value(value) + " run " + self.TreeDepth(depth, group)

    def Generate(self, pattern: Optimization):
        Path("items/depth0group0").mkdir(parents=True, exist_ok=True)

        with open("items/depth0group0", "w", encoding="utf-8") as output:
            output.write(self.Roll(pattern.count))

            for i in range(pattern.count):
                self.FullRandomDepth( i+1, 1, i)

        with open():






with open("items/output.txt", "w", encoding="utf-8") as output:
    output.write("Hello world\n")
