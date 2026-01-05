from optimizer import Optimizer
from reader import ItemContainer
from writer import Generator

optimizer = Optimizer(20) #8 should work as of 1/4/2026
reader = ItemContainer("All Items")
items = reader.GetItems()
itemCount = len(items)
pattern = optimizer.Partition(itemCount)
print(pattern)
writer = Generator()
writer.Generate(pattern, items)
