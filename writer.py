from pathlib import Path

from optimizer import Optimization


class Generator:
    itemIndex = 0
    def __init__(self):
        return
    def Give(self, text):
        return "give @s minecraft:" + text

    def Roll(self, size):
        return f"execute store result storage random:roll value int 1 run random value 1..{size}"

    def Value(self, value):
        return "execute if data storage random:roll {value:"+str(value)+"}"

    def TreeDepth(self, depth, group): #depth0group0
        return "function game:items/depth"+str(depth)+"group"+str(group)

    def FullRandomGive(self, value, text):
        return str(self.Value(value)) + " run " + self.Give(text)

    def FullRandomDepth(self, value, depth, group):
        return str(self.Value(value)) + " run " + self.TreeDepth(depth, group)

    def Generate(self, pattern, itemList):
        Path("items").mkdir(parents=True, exist_ok=True)
        self.itemIndex = -1
        self.RecursiveGenerate(pattern, itemList, 0, 0)
        print(f"Items Used: {self.itemIndex}")

    def RecursiveGenerate(self, pattern, itemList, currentDepth, currentGroup):
        if currentDepth == pattern.depth: return
        with (open(f"items/depth{currentDepth}group{currentGroup}.mcfunction", "w", encoding="utf-8") as output):
            output.write(self.Roll(pattern.count) + "\n")
            if currentDepth == pattern.depth - 1:
                for i in range(pattern.count):
                    output.write(self.FullRandomGive(i+1, self.GetNextItem(itemList)) + "\n")
            elif currentGroup == 0:
                for i in range(pattern.count):
                    output.write(self.FullRandomDepth(i+1, currentDepth + 1, i) + "\n")
                    self.RecursiveGenerate(pattern, itemList, currentDepth+1, i)
            else:
                for i in range(pattern.count):
                    output.write(self.FullRandomDepth(i+1, currentDepth + 1, currentGroup * pattern.count + i) + "\n")
                    self.RecursiveGenerate(pattern, itemList, currentDepth+1, currentGroup * pattern.count + i)

            # if currentGroup == 0:
            #     for i in range(pattern.count):
            #         output.write(self.FullRandomDepth(i+1, currentDepth + 1, i) + "\n")
            #         self.RecursiveGenerate(pattern, itemList, currentDepth+1, i)
            # elif currentDepth < pattern.depth - 1:
            #     for i in range(pattern.count):
            #         output.write(self.FullRandomDepth(i+1, currentDepth + 1, currentGroup * pattern.count) + "\n")
            #         self.RecursiveGenerate(pattern, itemList, currentDepth+1, currentGroup * pattern.count)
            # else:
            #     for i in range(pattern.count):
            #         output.write(self.FullRandomGive(i+1, self.GetNextItem(itemList)) + "\n")

    def GetNextItem(self, itemList):
        self.itemIndex += 1
        if self.itemIndex >= len(itemList): return "____"
        return itemList[self.itemIndex]