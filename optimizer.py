
class Optimization:
    def __init__(self, depth, count, maxLines):
        self.depth = depth
        self.count = count
        self.maxLines = maxLines
def partition(n):
    maxAttempts = 20;
    options = []
    for d in range(1, maxAttempts):
        x = 1
        while (x+1000)**d < n:
            x += 1000;
        while (x+100)**d < n:
            x += 100;
        while (x+10)**d < n:
            x += 10;
        while x**d < n:
            x += 1;
        options.append(Optimization(d, x, x*d + d))
    options.sort(key=lambda x: x.maxLines)
    return options[0]

result = partition(64);
print(f"Depth: {result.depth} | Group Size: {result.count} | Max: {result.maxLines}")
