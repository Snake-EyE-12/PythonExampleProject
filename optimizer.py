
class Optimization:
    def __init__(self, depth, count, maxLines):
        self.depth = depth
        self.count = count
        self.maxLines = maxLines

    def __str__(self):
        return f"Depth: {self.depth} | Group Size: {self.count} | Max: {self.maxLines}"


class Optimizer:
    def __init__(self, maxAttempts):
        self.maxAttempts = maxAttempts

    def Partition(self, n):
        options = []
        for d in range(1, self.maxAttempts):
            x = 1
            while (x + 1000) ** d < n:
                x += 1000;
            while (x + 100) ** d < n:
                x += 100;
            while (x + 10) ** d < n:
                x += 10;
            while x ** d < n:
                x += 1;
            options.append(Optimization(d, x, x * d + d))
        options.sort(key=lambda x: x.maxLines)
        return options[0]

o = Optimizer(20)
print(o.Partition(10))
print(o.Partition(20))