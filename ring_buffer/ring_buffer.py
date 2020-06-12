class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.newArray = []
        self.savedCap = capacity

    def append(self, item):
        if self.capacity > 0:
            # print("1")
            self.newArray.append(item)
            self.capacity -= 1
        elif self.capacity == 0:
            self.capacity = self.savedCap * -1
            # print("2")
            self.newArray[self.capacity] = item
            self.capacity += 1
        elif self.capacity < 0:
            # print("3")
            self.newArray[self.capacity] = item
            self.capacity += 1

    def get(self):
        return self.newArray