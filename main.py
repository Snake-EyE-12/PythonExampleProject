from optimizer import Optimizer

optimizer = Optimizer(20) #8 should work as of 1/4/2026
reader = ItemContainer("All Items")
optimizer.Partition()

reader.GetItems()

reader2 = ItemContainer("Bob")
reader2.GetItems()