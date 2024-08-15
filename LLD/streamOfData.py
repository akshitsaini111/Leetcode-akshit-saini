class StreamData:

    def __init__(self):
        self.maxVal = float("-inf")
        self.minVal = float("inf")

    def updateVal(self, val):
        if val > self.maxVal:
            self.maxVal = val
        if val < self.minVal:
            self.minVal = val

    def getMinVal(self):
        return self.minVal

    def getMaxVal(self):
        return self.maxVal


stream = StreamData()

# Simulating a stream of data
data = [5, 3, 8, 1, 9, 6]

for number in data:
    stream.updateVal(number)
    print(f"Current Min: {stream.getMinVal()}, Current Max: {stream.getMaxVal()}")
