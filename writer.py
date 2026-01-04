class Generator:
    def Give(self, text):
        return "give @s minecraft:" + text

    def Roll(self, size):
        return "execute store result storage random:roll value int 1 run random value 1.." + size
    def Value(self, value):
        return "execute if data storage random:roll {value:"+value+"}"

    def TreeDepth(self, depth, group): #depth0group0
        return "function game:depth"+depth+"group"+group

    def FullRandomGive(self, value, text):
        return self.Value(self, value) + " run " + self.Give(self, text)

    def FullRandomDepth(self, value, depth, group):
        return self.Value(self, value) + " run " + self.TreeDepth(self, depth, group)

    def Generate(self, pattern):
        return "done"






with open("output.txt", "w", encoding="utf-8") as output:
    output.write("Hello world\n")
